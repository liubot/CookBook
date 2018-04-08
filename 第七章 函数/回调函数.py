#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def app_sync(func,args,*,callback):
    result = func(*args)
    callback(result)

def print_result(result):
    print ("Get:",result)
def add(x,y):
    return x+y

app_sync(add,(2,3),callback=print_result)