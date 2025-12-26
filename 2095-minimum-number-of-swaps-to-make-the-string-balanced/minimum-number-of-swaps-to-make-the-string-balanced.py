class Solution:
    def minSwaps(self, s: str) -> int:
        opening = 0
        res = 0
        for c in s:
            if c == '[':
                opening += 1
            elif opening > 0:
                opening -= 1
            else:
                res += 1
        
        return (res + 1) // 2