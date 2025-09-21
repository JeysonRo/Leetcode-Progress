class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums, perm):
            if len(nums) == 0:
                res.append(perm.copy())
                return

            for i, val in enumerate(nums):
                dfs(nums[:i] + nums[i+1:], perm + [val])
        
        dfs(nums, [])
        return res