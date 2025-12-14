class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        if len(self.output_stack) > 0:
            return self.output_stack.pop()
        elif len(self.input_stack) > 0:
            for i in range(len(self.input_stack)):
                self.output_stack.append(self.input_stack.pop())
            return self.output_stack.pop()
        else:
            return None

    def peek(self) -> int:
        if len(self.output_stack) > 0:
            return self.output_stack[-1]
        elif len(self.input_stack) > 0:
            return self.input_stack[0]
        else:
            return None

    def empty(self) -> bool:
        return len(self.input_stack) == 0 and len(self.output_stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()