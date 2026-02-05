class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        dp = [0 for i in range(N)]

        if costs[2] < costs[1]:
            costs[1] = costs[2]
        if costs[1] < costs[0]:
            costs[0] = costs[1]

        def dfs(i):
            if i == N:
                return 0
            if dp[i] != 0:
                return dp[i]

            dp[i] = float("inf")
            for d, c in zip([1, 7, 30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dfs(j))
            return dp[i]
        
        return dfs(0)