class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            lchar = s[l].lower()
            rchar = s[r].lower()
            if lchar != rchar:
                return False
            l += 1
            r -= 1
        
        return True