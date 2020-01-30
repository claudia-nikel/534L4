#!/usr/bin/env python
import sys
import os
import collections
import functools
import operator

x=[]
dic={}

# sum the values with same keys
for line in sys.stdin:
    line = line.strip().split('\t')
    dic[line[0]] = int(line[1])
    x.append(dic)

result = dict(functools.reduce(operator.add,map(collections.Counter, x)))

print(str(result))
