class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for i in tokens:
            if i == '+':
                p2 = stack.pop()
                p1 = stack.pop()
                stack.append(p1 + p2)
            elif i == '-':
                p2 = stack.pop()
                p1 = stack.pop()
                stack.append(p1 - p2)
            elif i == '*':
                p2 = stack.pop()
                p1 = stack.pop()
                stack.append(p1 * p2)
            elif i == '/':
                p2 = stack.pop()
                p1 = stack.pop()
                res = p1 / p2
                if res > 0:
                    res = math.floor(res)
                else:
                    res = math.ceil(res)
                stack.append(res)
            else:
                stack.append(int(i))
                continue
        
        return stack.pop()