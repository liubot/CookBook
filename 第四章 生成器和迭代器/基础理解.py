#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def frange(start,end,step):
    while start <= end:
        yield start
        start += step

print (list(frange(1,10,0.4)))
