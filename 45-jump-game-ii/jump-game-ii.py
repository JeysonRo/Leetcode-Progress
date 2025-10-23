class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [len(nums) for i in range(len(nums))]
        dp[0] = 0
        i = 0
        j = 1
        while i < len(nums):
            while j <= i + nums[i] and j < len(nums):
                dp[j] = dp[i] + 1
                j += 1
            i += 1
                
        return dp[len(nums)-1]