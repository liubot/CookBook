#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import heapq
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1

    def pop(self):
        return (heapq.heappop(self._queue)[-1])


class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)




p = PriorityQueue()
p.push(Item("liubo"),5)
p.push(Item("hanxue"),3)
p.push(Item("baby"),6)
print (type(p.pop()))
print (p.pop())
p.pop()
