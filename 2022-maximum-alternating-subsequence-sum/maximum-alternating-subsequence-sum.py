class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        cache = {} # (i, add) : sum

        def dfs(i, add):
            if i >= len(nums):
                return 0
            if (i, add) in cache:
                return cache[(i, add)]
            # include
            if add:
                res = dfs(i + 1, not add) + nums[i]
            else:
                res = dfs(i + 1, not add) - nums[i]
            # skip
            res = max(res, dfs(i + 1, add))
            cache[(i, add)] = res
            return res

        return dfs(0, True) 