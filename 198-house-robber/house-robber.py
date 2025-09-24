class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        
        memo = [0 for i in range(4)]


        memo[0] = nums[0]
        memo[1] = max(nums[1], memo[0])
        memo[2] = max(nums[2] + nums[0], nums[1])
        i = 3
        
        while i < (len(nums)):
            memo[3] = nums[i] + max(memo[1], memo[0])

            i += 1
            for j in range(len(memo) - 1):
                memo[j] = memo[j+1]
        
        return max(memo[-1], memo[-3])
