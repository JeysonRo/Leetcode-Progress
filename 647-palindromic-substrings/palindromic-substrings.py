class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPali(s:str):
            l = 0
            r = len(s)-1
            if s[l] != s[r]:
                return False
            return True
        
        if len(s) == 1:
            return 1
        palindromes = 0

        # odd
        l = r = 0
        while r < len(s):
            l2 = 0
            r2 = 0
            while l - l2 >= 0 and r + r2 < len(s) and isPali(s[l - l2:r + r2+1]):
                l2 += 1
                r2 += 1
                palindromes += 1
                #reset r and l
            l += 1
            r += 1

        # even
        l = 0
        r = 1
        while r < len(s):
            l2 = 0
            r2 = 0
            while l - l2 >= 0 and r + r2 < len(s) and isPali(s[l - l2:r + r2+1]):
                l2 += 1
                r2 += 1
                palindromes += 1

            l+=1
            r+=1
        
        return palindromes
