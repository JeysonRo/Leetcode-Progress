class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def pa(openp: int, closep: int):
            if openp == closep == 0:
                res.append("".join(stack))
                return
            if openp > 0:
                stack.append("(")
                pa(openp - 1, closep)
                stack.pop()
            if closep > openp:
                stack.append(")")
                pa(openp, closep - 1)
                stack.pop()
        
        pa(n, n)
        return res
