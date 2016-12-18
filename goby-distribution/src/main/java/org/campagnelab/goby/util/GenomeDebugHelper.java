package org.campagnelab.goby.util;

import it.unimi.dsi.lang.MutableString;
import org.campagnelab.goby.reads.RandomAccessSequenceInterface;

/**
 * Helper to look at genomic positions while debugging.
 * Created by fac2003 on 12/17/16.
 */
public class GenomeDebugHelper {
    public static void showLocation(RandomAccessSequenceInterface genome, int genomeTargetIndex, int keyPos) {
        MutableString before = new MutableString();
        MutableString after = new MutableString();
        char base;
        genome.getRange(genomeTargetIndex, keyPos - 10, 10, before);
        genome.getRange(genomeTargetIndex, keyPos + 10, 10, after);
        base = genome.get(genomeTargetIndex, keyPos);
        System.out.printf("%s:%d %s|%c|%s%n", genome.getReferenceName(genomeTargetIndex),
                keyPos, before, base, after
        );
    }
}
