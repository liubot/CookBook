#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from urllib import request
class UrlTemplate:
    def __init__(self,template):
        self.template = template

    def open(self,**kwargs):
        return request.urlopen(self.template.format_map(kwargs))

# baidu = UrlTemplate("http://www.baidu.com/s?wd={name}")
# for line in baidu.open(name="girl"):
#     print (line.decode("utf-8"))

def UrlTem(template):
    def opener(**kwargs):
        return request.urlopen(template.format_map(kwargs))
    return opener
baidu = UrlTem("http://www.baidu.com/s?wd={name}")
for line in baidu(name="girl"):
    print (line.decode("utf-8"))

