class lazyproperty:
    def __init__(self,func):
        self.func = func
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance,self.func.__name__,value)
            return value
import cmath
class Cricle:
    def __init__(self,radius):
        self.radius = radius
    @lazyproperty
    def area(self):
        print ("Computing area!")
        return cmath.pi*self.radius**2
    @lazyproperty
    def zhouchang(self):
        print ("zhou chang")
        return 2*cmath.pi*self.radius

c = Cricle(4)
print (c.area)
print (c.zhouchang)
print (c.area)
print (c.zhouchang)
print (vars(c))
print (c.__dict__)

d = Cricle(5)
print (d.area)
print (d.area)