class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) <= 3:
            return max(nums)
        memo = [nums[0]] * len(nums)
        memo[0] = nums[0]
        memo[1] = max(memo[0], nums[1])
        memo[2] = max(memo[0] + nums[2], memo[1])
        i = 3
        while i < len(nums) - 1: # one before end
            memo[i] = nums[i] + max(memo[i-2], memo[i-3])
            i+=1

        rob1 = max(memo[-3], memo[-2])

        i = 4
        memo[1] = nums[1]
        memo[2] = max(memo[1], nums[2])
        memo[3] = max(memo[1] + nums[3], memo[2])

        while i < len(nums):
            memo[i] = nums[i] + max(memo[i-2], memo[i-3])
            i+=1
        rob2 = max(memo[-3], memo[-2], memo[-1])

        return max(rob1, rob2)