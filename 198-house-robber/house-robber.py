class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        
        memo = [0 for i in range(len(nums))]
        
        memo[0] = nums[0]
        memo[1] = max(nums[1], memo[0])
        memo[2] = max(nums[2] + nums[0], nums[1])
        i = 3
        
        while i < (len(nums)):
            memo[i] = nums[i] + max(memo[i-2], memo[i-3])
            i += 1
        
        return max(memo[-1], memo[-2])
