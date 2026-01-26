class Solution:
    def knightDialer(self, n: int) -> int:
        digits = [[] for i in range(10)]

        digits[0] = [4,6]
        digits[1] = [6,8]
        digits[2] = [7,9]
        digits[3] = [4,8]
        digits[4] = [0,3,9]
        digits[5] = []
        digits[6] = [0,1,7]
        digits[7] = [2,6]
        digits[8] = [1,3]
        digits[9] = [2,4]

        @lru_cache(None)
        def dfs(digit, n):
            if n == 1:
                return 1
            res = 0
            for nei in digits[digit]:
                res += dfs(nei, n-1)
            return res

        res = 0
        for i in range(10):
            res += dfs(i, n)
            res %= (10**9 + 7)
        
        return res % (10**9 + 7)