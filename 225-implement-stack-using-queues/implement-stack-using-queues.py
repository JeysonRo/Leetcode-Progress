class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.appendleft(x)

    def pop(self) -> int:
        for i in range(len(self.queue) - 1):
            res = self.queue.pop()
            self.queue.appendleft(res)
        return self.queue.pop()

    def top(self) -> int:
        for i in range(len(self.queue)):
            res = self.queue.pop()
            self.queue.appendleft(res)
        return res

    def empty(self) -> bool:
        if not self.queue:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()