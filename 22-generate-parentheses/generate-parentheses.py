class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(n, stack, combination):
            if n == 0:
                while stack > 0:
                    stack -= 1
                    combination += ")"
                res.append(combination)
                return
            
            if stack == 0:
                backtrack(n-1, stack+1, combination + "(")
            else:
                backtrack(n-1, stack+1, combination + "(")
                backtrack(n, stack-1, combination + ")")
        
            return

        backtrack(n, 0, '')
        return res