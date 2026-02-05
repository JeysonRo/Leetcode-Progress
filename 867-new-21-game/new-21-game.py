class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        if k == 0 or k + maxPts <= n:
            return 1.0
        
        windowSum = 0
        dp = {}
        for i in range(k, k + maxPts):
            if i <= n:
                dp[i] = 1
            else:
                dp[i] = 0
            windowSum += dp[i]
        
        for i in range(k - 1, -1, -1):
            dp[i] = windowSum / maxPts
            windowSum += dp[i]
            windowSum -= dp[i + maxPts]
            del dp[i + maxPts]

        return dp[0]