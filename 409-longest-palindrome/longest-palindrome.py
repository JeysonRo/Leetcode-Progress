class Solution:
    def longestPalindrome(self, s: str) -> int:
        bank = {}

        for c in s:
            bank[c] = bank.get(c, 0) + 1
        
        odd = False
        res = 0
        for val in bank.values():
            res += val - (val % 2)
            if val % 2 == 1:
                odd = True
        return res+1 if odd else res