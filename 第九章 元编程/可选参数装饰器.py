from functools import wraps,partial
import logging

def logged(func=None,*,level=logging.DEBUG,name=None,message=None):
    if func is None:
        return partial(logged,level=level,name=name,message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args,**kwargs):
        log.log(level,logmsg)
        return func(*args,**kwargs)
    return wrapper

@logged # logged(add)(3,4)
def add(x,y):
    print (x+y)

@logged(level=logging.CRITICAL,name="example") #logged(level=logging.CRITICAL,name="example")(add)
def spam():
    print("Spam")


spam()
add(3,4)