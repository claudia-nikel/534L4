#!/usr/bin/env python

import sys

keyword = "google"
number_word = {}
for line in sys.stdin:
    words = line.split("\t")
    
    if keyword.lower() in words[0].lower():
        print("{}\t{}\t{}".format(words[0],words[1],words[2]))
