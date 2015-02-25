class MinStack:
    """
    [1, 4, 5, 5, 7, 0, 8]
    [1, 4, 5, 5, 7, 8]
    """
    def __init__(self):
        self.__stack = []
        self.__min = []

    def push(self, x):
        self.__stack.append(x)
        if self.min_top() is not None:
            if x <= self.min_top():
                self.__min.append(x)
        else:
            self.__min.append(x)

    # @return nothing
    def pop(self):
        if self.top() == self.min_top():
            self.__min.pop()
        self.__stack.pop()

    # @return an integer
    def top(self):
        if len(self.__stack) == 0:
            return None
        else:
            return self.__stack[-1]

    def min_top(self):
        if len(self.__min) == 0:
            return None
        else:
            return self.__min[-1]

    # @return an integer
    def getMin(self):
        return self.min_top()

lol = MinStack()
