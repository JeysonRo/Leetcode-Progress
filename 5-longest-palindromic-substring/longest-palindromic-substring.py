class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPali(string: str):
            l = 0
            r = len(string) - 1
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        l = 0
        r = 1
        longest = s[0]
        swap = True

        while r < len(s):
            if isPali(s[l:r + 1]):
                longest = s[l:r+1]
                if l == 0:
                    r += 1
                else:
                    l -= 1
                swap = True
                continue
            if swap:
                r += 1
            else:
                l += 1
            swap = not swap

        return longest