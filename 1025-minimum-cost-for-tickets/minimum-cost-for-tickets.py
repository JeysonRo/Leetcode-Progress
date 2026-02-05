class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        dp = [float('inf') for i in range(N)]
        dp.append(0)

        for i in range(N - 1, -1, -1):
            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < N and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dp[j])
        
        return dp[0]