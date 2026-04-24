class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        table = {}
        table['2'] = ['a','b','c']
        table['3'] = ['d','e','f']
        table['4'] = ['g','h','i']
        table['5'] = ['j','k','l']
        table['6'] = ['m','n','o']
        table['7'] = ['p','q','r','s']
        table['8'] = ['t','u','v']
        table['9'] = ['w','x','y','z']

        res = []
        def recurs(cur, i):
            if len(cur) == len(digits):
                res.append(cur)
                return
            for letter in table[digits[i]]:
                recurs(cur + letter, i+1)
        recurs("", 0)
        return res