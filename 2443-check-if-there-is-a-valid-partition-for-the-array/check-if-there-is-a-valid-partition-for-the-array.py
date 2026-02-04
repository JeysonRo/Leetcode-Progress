class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        N = len(nums)

        @cache
        def dfs(i):
            if i == N:
                return True
            if i + 2 < N:
                if nums[i] == nums[i+1] - 1 and nums[i+1] == nums[i+2] - 1:
                    save = dfs(i+3)
                    if save:
                        return True
                if nums[i] == nums[i+1] and nums[i] == nums[i+2]:
                    save = dfs(i+3)
                    if save:
                        return True
            if i + 1 < N:
                if nums[i] == nums[i+1]:
                    save = dfs(i+2)
                    if save:
                        return True
            return False
        
        return dfs(0)