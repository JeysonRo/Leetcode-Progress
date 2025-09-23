class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        i = 2
        a = 1
        b = 2
        while i < n:
            c = a + b
            a = b
            b = c
            i += 1
        return b