__author__ = 'aouyang1'

from Node import Node


class Stack(object):

    def __init__(self):
        self.top = None
        self.num_elem = 0

    def push(self, item):
        if not self.top:
            self.top = Node(item)
        else:
            old_top = self.top
            self.top = Node(item)
            self.top.next = old_top

        self.num_elem +=1

    def pop(self):
        if not self.top:
            return False
        else:
            item = self.top.data
            self.top = self.top.next
            self.num_elem -= 1
            return item

    def peek(self):
        if not self.top:
            return None
        else:
            item = self.top.data
            return item

    def isEmpty(self):
        return not self.top

    def size(self):
        return self.num_elem
