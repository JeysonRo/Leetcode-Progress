class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, v):
            if (i, v) in dp:
                return dp[(i, v)]
            if i == len(nums):
                if v == target:
                    return 1
                else:
                    return 0
            dp[(i, v)] = dfs(i+1, v + nums[i]) + dfs(i+1, v - nums[i])
            return dp[(i, v)]
        
        return dfs(0,0)
            