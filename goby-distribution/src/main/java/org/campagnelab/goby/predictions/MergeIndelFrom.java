package org.campagnelab.goby.predictions;

import it.unimi.dsi.fastutil.objects.ObjectArraySet;
import org.apache.commons.lang.StringUtils;
import org.campagnelab.goby.util.Variant;

import java.io.Serializable;
import java.util.Set;

/**
 Example:
 A -> T
 A -> A
 ATTTGC -> A-TTGC
 A--TTTG -> ATTTTG

 Step 1: get longest tail after indel: TTGC
 Step 2: replace all tails with longest tail

 ATTTGC TTTTGC
 ATTTGC ATTTGC
 ATTTGC A-TTGC
 A--TTTGC ATTTTGC

 Step 3: get max number of dashes in from: 2
 Step 4:  append dashes to ins and del fields until all have maxFromDash

 A--TTTGC T--TTTGC
 A--TTTGC A--TTTGC
 A--TTTGC A---TTGC
 A--TTTGC ATTTTGC

 Approach:
 Split every indel into:
 refBase, ins, del, tail
 (one of ins, del will contain only dashes.)
 Then process steps above

 */
public class MergeIndelFrom {


    Set<String> tos = new ObjectArraySet<>();
    String from;


    public Set<String> getTos() {
        return tos;
    }

    public String getFrom() {
        return from;
    }

    static public class SplitIndel {

        char baseFrom;
        char baseTo;
        String insFrom; //empty or contains only dashes
        String delFrom; //bases in ref genome that are deleted
        String insTo; //new bases introduced
        String delTo; //empty or contains only dashes
        String tail;
        //number of bases from genome represented by concatenating delFrom and tail.
        int lenDelFromAndTail = 0;
        //number of deleted bases
        int delLen = 0;
        //number of inserted bases
        int insLen = 0;


        /**
         * @param fromTo
         * Does not support multiple indels at once, ie from:ATTTTGC -> A-TTT-C
         * Probably does not support already padded indels (ie indels with dashes in both to and from fields.
         * Assumes that from and to field are the same length
         * Assumes that the the first base of both are the position before the first "-".
         */
        public SplitIndel(Variant.FromTo fromTo){
            baseFrom = fromTo.getFrom().charAt(0);
            baseTo = fromTo.getTo().charAt(0);
            delLen = StringUtils.countMatches(fromTo.getTo(),"-");
            insLen = StringUtils.countMatches(fromTo.getFrom(),"-");
            if (delLen==0 && insLen==0){
                //handle snp or ref
                insFrom = "";
                delFrom = "";
                insTo = "";
                delTo = "";
                this.tail = fromTo.getTo().substring(1);
                return;
            }
            //general approach: from = base + insFrom + delFrom + tail, to = base + insTo + delTo + tail.
            //we will split, and later be able to padd all fields as needed and reconcat.
            insFrom = fromTo.getFrom().substring(1,insLen+1);
            insTo = fromTo.getTo().substring(1,insLen+1);
            delFrom = fromTo.getFrom().substring(1+insLen,1+insLen+delLen);
            delTo = fromTo.getTo().substring(1+insLen,1+insLen+delLen);
            tail = fromTo.getTo().substring(1+insLen+delLen,fromTo.getTo().length());
            lenDelFromAndTail = delFrom.length() + tail.length();
        }


        String getFrom(){
            return baseFrom + insFrom + delFrom + tail;
        }

        String getTo(){
            return baseTo + insTo + delTo + tail;
        }
    }

    /**
     * Contract assumptions:
     * Refs and snps are of the form from:a to:b.
     * Insertions are of the form from:a--defg to:abcdefg
     * Deletions are of the form from:abcdefg to: a--defg
     * @param fromTos
     */

    public MergeIndelFrom(Set<Variant.FromTo> fromTos){
        Set<SplitIndel> splits = new ObjectArraySet<>(fromTos.size());
        //split up each indel into component strings
        for (Variant.FromTo fromTo : fromTos){
            splits.add(new SplitIndel(fromTo));
        }

        //find longest delFrom+tail and replace all genotypes' tails with the longest
        String longestDfAndTail = "";
        int maxLen = 0;
        for (SplitIndel split : splits){
            if (split.lenDelFromAndTail > maxLen){
                maxLen = split.lenDelFromAndTail;
                longestDfAndTail = split.delFrom + split.tail;
            }
        }
        for (SplitIndel split : splits){
            if (split.lenDelFromAndTail < maxLen){
                split.tail = longestDfAndTail.substring(split.delFrom.length());
            }
        }



        //get max dashes ins:from (aka length of ins:from)
        int maxDashLen = 0;
        for (SplitIndel split : splits){
            maxDashLen = Math.max(maxDashLen,split.insLen);
        }

        String maxDashToAppend = new String(new char[maxDashLen]).replace("\0", "-");
        //append dashes to all inserts and dels so that "from" fields have same dash count
        for (SplitIndel split : splits){
            int numDashToAdd = maxDashLen - split.insLen;
            split.insFrom = maxDashToAppend.substring(0,numDashToAdd) + split.insFrom;
            split.insTo = maxDashToAppend.substring(0,numDashToAdd) + split.insTo;
        }


        //populate fields for output from split indels
        for (SplitIndel split : splits){
            tos.add(split.getTo());
            if (from==null){
                from = split.getFrom();
            } else {
                assert from.equals(split.getFrom());
            }
        }

    }
}
