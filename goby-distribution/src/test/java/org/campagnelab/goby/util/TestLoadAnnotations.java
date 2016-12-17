/*
 * Copyright (C) 2009-2012 Institute for Computational Biomedicine,
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

package org.campagnelab.goby.util;

import org.campagnelab.goby.modes.CompactAlignmentToAnnotationCountsMode;
import org.junit.Test;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

import static junit.framework.Assert.assertNotNull;

/**
 * @author Fabien Campagne
 *         Date: 9/4/12
 *         Time: 5:23 PM
 */
public class TestLoadAnnotations {
    // @Test
    // The data directory was removed from the goby 3 repo (too large). TODO: migrate this test to use a small annotation file placed under test-data
    public void loadAnnotations() throws IOException {


        assertNotNull(CompactAlignmentToAnnotationCountsMode.readAnnotations(new FileReader(new File("data/annotations/methyl-cpgIsland-annotations.tsv"))));
        assertNotNull(CompactAlignmentToAnnotationCountsMode.readAnnotations(new FileReader(new File("data/annotations/methyl-ens-promoter-annotations.tsv"))));
    }
}
