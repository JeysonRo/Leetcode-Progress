# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        l = 1
        r = n

        while l <= r:
            i = l + (r - l) // 2
            isbad = isBadVersion(i)
            if isbad:
                r = i - 1
            else:
                l = i + 1
        
        return r + 1