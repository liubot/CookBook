import cmath
class Structure1:
    _fields = []
    def __init__(self,*args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        else:
            for name,value in zip(self._fields,args):
                setattr(self,name,value)

class student(Structure1):
    _fields = ["name","age"]

class Point(Structure1):
    _fields = ["x","y"]

s = student("liubo",9)
print (s.name)