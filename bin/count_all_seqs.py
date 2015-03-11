#!/usr/bin/env python

import sys
import fnmatch
import os
import seq_utils

if len(sys.argv) < 2:
        print "count_all_seqs.py expects a directory name as an argument"
else:
        for filename in sorted(os.listdir(sys.argv[1])):
                if fnmatch.fnmatch(filename, '*.fasta'):
                        fullpath = os.path.join(sys.argv[1],filename)
                        input_file = open(fullpath)
                        seq_count = seq_utils.count_seqs(input_file)
                        print filename,seq_count
