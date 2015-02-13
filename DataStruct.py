__author__ = 'aouyang1'

from Node import Node


class StackClass(object):

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

    def is_empty(self):
        return not self.top

    def size(self):
        return self.num_elem


class QueueClass(object):

    def __init__(self):
        self.front = None
        self.rear = None
        self.num_elem = 0

    def enqueue(self, item):
        if not self.rear:
            self.rear = Node(item)
            self.front = self.rear
        else:
            old_rear = self.rear
            self.rear = Node(item)
            self.rear.next = old_rear
            old_rear.prev = self.rear

        self.num_elem += 1

    def dequeue(self):
        if not self.front:
            return False
        else:
            item = self.front.data
            print self.front.prev, self.size()
            self.front = self.front.prev
            self.front.next = None
            self.num_elem -= 1
            return item

    def is_empty(self):
        return not self.rear

    def size(self):
        return self.num_elem