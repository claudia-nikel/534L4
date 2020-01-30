#!/usr/bin/env python

import sys

words_data = {}

for line in sys.stdin:
    word, year, count = line.split("\t")
    
    try:
        words_data[year.strip()] += int(count.strip())
    except KeyError:
        words_data[year.strip()] = int(count.strip())

for year, count in words_data.items():
    print("{}\t{}".format(year,count))