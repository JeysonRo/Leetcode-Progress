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

        mod = (10**9 + 7)

        dp = [1 for i in range(10)]
        cur = 1
        while cur < n:
            next_dp = [0 for i in range(10)]
            for i in range(10):
                for digit in digits[i]:
                    dp[i] = dp[i] % mod
                    next_dp[i] += dp[digit]
            dp = next_dp
            cur += 1
        
        res = 0
        for val in dp:
            res += val % mod

        return res % mod