#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from collections import ChainMap
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
c = ChainMap(a,b)

a["z"]=6
print (c.get("z"))
a["name"]="liubo"
for item in c.items():
    print (item)