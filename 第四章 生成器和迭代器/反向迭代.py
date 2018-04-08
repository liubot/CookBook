#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class CountDown:
    def __init__(self,start):
        self.start = start
    def __iter__(self):
        n = self.start
        while n >0 :
            yield  n
            n -= 1
    def __reversed__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
for rr in CountDown(10):
    print (rr)

for rr in reversed(CountDown(10)):
    print(rr)