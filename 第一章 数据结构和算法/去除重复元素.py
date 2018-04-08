#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def deque(items,key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)




list1=[1,8,2,3,2,5,42,3,]
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(deque(a,key=lambda d:(d["x"],d["y"]))))