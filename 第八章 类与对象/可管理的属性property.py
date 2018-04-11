#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class Person:
    def __init__(self,first_name,age):
        self.age = age
        self._first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self,val):
        if not isinstance(val,str):
            raise TypeError("Expected a string")
        self._first_name = val

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

a = Person(33,27)
print (a.first_name)
print (a.age)
a.age = 28
a.first_name="hanxue"
print (a.first_name)
