# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # binary search

        l = 1
        r = n

        while l <= r:
            i = (l + r) // 2
            bad = isBadVersion(i)
            if bad:
                r = i - 1
            else:
                l = i + 1

        return r + 1            