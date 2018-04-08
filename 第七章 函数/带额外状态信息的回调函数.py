#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def app_sync(func,args,*,callback):
    res = func(*args)
    callback(res)

def add(x,y):
    return x+y

class Handle:
    def __init__(self):
        self.num = 0
    def handle(self,data):
        self.num += 1
        print ("[{}] data:{}".format(self.num,data))

def Handle2():
    num = 0
    def handle(data):
        nonlocal num
        num +=1
        print ("[{}] data: {}".format(num,data))
    return handle


obj = Handle()
res = app_sync(add,(4,5),callback=obj.handle)
res = app_sync(add,(4,9),callback=obj.handle)

app_sync(add,(4,3),callback=Handle2())





