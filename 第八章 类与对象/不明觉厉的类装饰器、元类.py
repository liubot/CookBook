#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Descriptor:
    def __init__(self,name=None,**opts):
        self.name = name
        for key,value in opts.items():
            setattr(self,key,value)
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class Typed(Descriptor):
    expected_type = type(None)
    def __set__(self, instance, value):
        if not isinstance(value,self.expected_type):
            raise TypeError("Expected {}".format(self.expected_type))
        super().__set__(instance,value)

class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Expected >= 0")
        super().__set__(instance,value)

class MaxSized(Descriptor):
    def __init__(self,name=None,**opts):
        if "size" not in opts:
            raise TypeError("missing size option")
        super().__init__(name,**opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError("size must be < {}".format(self.size))
        super().__set__(instance,value)


class Integer(Typed):
    expected_type = int

class UnsignedInteger(Integer,Unsigned):
    pass

class Float(Typed):
    expected_type = float

class UnsignedFloat(Float,Unsigned):
    pass

class String(Typed):
    expected_type = str

class SizeString(String,MaxSized):
    pass



class Stock:
    name = SizeString('name',size=8)
    shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
s = Stock("apple",5,12.01)
print (s.name)
print (s.shares)
s.shares = 10

'''类装饰器'''
def check_attributes(**kwargs):
    def decorate(cls):
        for key,value in kwargs.items():
            if isinstance(value,Descriptor):
                value.name = key
                setattr(cls,key,value)
            else:
                setattr(cls,key,value(key))
        return cls
    return decorate

@check_attributes(name=SizeString(size=8),shares=UnsignedInteger,price=UnsignedFloat)
class Stock2:
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price

'''元类'''
