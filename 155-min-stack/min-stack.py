from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.Min = None

    def push(self, val: int) -> None:
        self.stack.append((val, self.Min))
        if self.Min == None:
            self.Min = val
        else:
            self.Min = min(self.Min, val)
        
    def pop(self) -> None:
        stuff = self.stack.pop()
        self.Min = stuff[1]


    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.Min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()