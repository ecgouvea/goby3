/*
 * Copyright (C) 2009-2011 Institute for Computational Biomedicine,
 *                    Weill Medical College of Cornell University
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

package org.campagnelab.goby.algorithmic.data.xml;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;

/**
 * @author Fabien Campagne
 *         Date: 10/23/11
 *         Time: 5:46 PM
 */
@XmlAccessorType(XmlAccessType.FIELD)
public class SampleTotalCount {
    /**
     * Sample identifier.
     */
    public String sampleId;
    /**
     * Total number of reads that mapped when sample was aligned to the reference.
     */
    public long totalCount;

    @Override
    public String toString() {
        final StringBuffer sb=new StringBuffer();
        sb.append("sample-id: ");
        sb.append(sampleId);
        sb.append("total-count: ");
        sb.append(totalCount);
        return sb.toString();
    }
}