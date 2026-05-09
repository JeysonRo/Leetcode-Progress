class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_bank = {}

        for c in s:
            letter_bank[c] = 1 + letter_bank.get(c, 0)
        
        res = 0
        odd = False
        for i in letter_bank.keys():
            if letter_bank[i] >= 2:
                val = letter_bank[i] // 2
                letter_bank[i] = letter_bank[i] % 2
                res += val * 2
            
            if not odd and letter_bank[i] > 0:
                res += 1
                odd = True
        
        return res