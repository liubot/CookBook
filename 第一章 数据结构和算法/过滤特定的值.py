#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def is_int(item):
    try:
        int(item)
        return True
    except Exception:
        return False

nums = [1,2,"4","8","hell",3,4,"99"]

print (list(filter(is_int,nums)))

