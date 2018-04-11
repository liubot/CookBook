import cmath

class Structure1:
    _fields = []
    def __init__(self,*args,**kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        for name,value in zip(self._fields,args):
            setattr(self,name,value)
        for name in self._fields[len(args):]:
            setattr(self,name,kwargs.pop(name))
        if kwargs:
            raise TypeError("Invalid arguments {}".format(",".join(kwargs)))


class student(Structure1):
    _fields = ["name","age"]

class Point(Structure1):
    _fields = ["x","y","doit"]

# s = student("liubo",9)
p = Point(3,9,doit=55)
print (p.doit)