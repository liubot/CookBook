#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Integer:
    def __init__(self,name):
        self.name = name

    def __get__(self,instance,cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
    def __set__(self,instance,value):
        if not isinstance(value,int):
            raise TypeError("Expected an int")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

class Point:
    x = Integer('x')
    y = Integer('y')
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

p = Point(2,3,5)
print (p.x)
p.y = 5
del p.y
print (p.__dict__)



