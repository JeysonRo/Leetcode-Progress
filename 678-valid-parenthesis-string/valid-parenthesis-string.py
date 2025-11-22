class Solution:
    def checkValidString(self, s: str) -> bool:
        wild = 0
        left_parentheses = 0

        for c in s:
            if c == "*":
                wild += 1
                left_parentheses -= 1
                if left_parentheses < 0:
                    left_parentheses = 0
            elif c == "(":
                left_parentheses += 1
                wild += 1
            elif c == ")":
                if left_parentheses > 0:
                    left_parentheses -= 1
                    wild -= 1
                else:
                    if wild > 0:
                        wild -= 1
                    else:
                        return False
        if left_parentheses > 0:
            return False
        return True