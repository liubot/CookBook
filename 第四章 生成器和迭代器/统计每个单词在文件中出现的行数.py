#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from collections import defaultdict
word_dict = defaultdict(list)

with open("song") as f:
    lines = f.readlines()

for no,line in enumerate(lines):
    words = (w.strip().lower() for w in line.split())
    for word in words:
        word_dict[word].append(no)
for i in word_dict.items():
    print (i)