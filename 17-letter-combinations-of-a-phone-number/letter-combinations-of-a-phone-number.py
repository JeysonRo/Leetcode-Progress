class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) <= 0:
            return []
        table = dict()
        table['2'] = 'abc'
        table['3'] = 'def'
        table['4'] = 'ghi'
        table['5'] = 'jkl'
        table['6'] = 'mno'
        table['7'] = 'pqrs'
        table['8'] = 'tuv'
        table['9'] = 'wxyz'

        res = []
        cur = []

        def dfs(i):
            if i >= len(digits):
                res.append(''.join(cur))
                return
            for j in table[digits[i]]:
                cur.append(j)
                dfs(i + 1)
                cur.pop()
        
        dfs(0)
        return res