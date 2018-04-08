#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class FileReverse:
    def __init__(self,file):
        self.file=file
    def __iter__(self):
        with open(self.file) as f:
            for line in f:

