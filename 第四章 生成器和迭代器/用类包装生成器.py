#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from collections import deque
class LineHistory:
    def __init__(self,lines,search,histen=3):
        self.lines = lines
        self.search = search
        self.history = deque(maxlen=histen)

    def __iter__(self):
        for no,line in enumerate(self.lines,1):
            if self.search in line:
                self.history.append((no,line))
                yield line
    def clear(self):
        self.history.clear()

with open("song") as f:
    lines = LineHistory(f,"You")
    for line in lines:
        print (line)
    print (lines.history)

