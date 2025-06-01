class Solution:
    def isValid(self, s: str) -> bool:

        stack = deque()

        for c in s:
            if c == "(":
                stack.append("(")
            elif c == "{":
                stack.append("{")
            elif c == "[":
                stack.append("[")

            elif c == ")":
                if not stack:
                    return False
                temp = stack.pop()
                if temp != "(":
                    return False
            elif c == "}":
                if not stack:
                    return False
                temp = stack.pop()
                if temp != "{":
                    return False
            elif c == "]":
                if not stack:
                    return False
                temp = stack.pop()
                if temp != "[":
                    return False
        
        if stack:
            return False
        else:
            return True

