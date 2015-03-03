"""
>>> stack = MinStack()
>>> stack.push(5)
>>> stack.push(1)
>>> stack.push(2)
>>> stack.push(3)
>>> stack.push(7)
>>> stack.push(4)
>>> stack.top()
4
>>> stack.pop()
>>> stack.top()
7
>>> stack.get_min()
1
>>> stack.pop()
>>> stack.get_min()
1
>>> stack.pop()
>>> stack.get_min()
1
>>> stack.pop()
>>> stack.get_min()
1
>>> stack.pop()
>>> stack.get_min()
5
"""


class MinStack(object):
    """ Min Stack """

    def __init__(self):
        self.__my_list = []
        self.__min_list = []

    def push(self, x):
        self.__my_list.append(x)
        if not self.__min_list or x <= self.__min_list[-1]:
            self.__min_list.append(x)

    def pop(self):
        if self.__my_list:
            val = self.__my_list.pop()
            if val == self.get_min():
                self.__min_list.pop()

    def top(self):
        return self.__my_list[-1]

    def get_min(self):
        return self.__min_list[-1]