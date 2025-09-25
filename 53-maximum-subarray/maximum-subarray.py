class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        
        l = 0

        while l < len(nums) and nums[l] < 0:
            maxsum = max(maxsum, nums[l])
            l += 1
        if l == len(nums):
            return maxsum

        cursum = 0
        while l < len(nums):
            cursum += nums[l]
            if cursum <= 0:
                cursum = 0
            if cursum > maxsum:
                maxsum = cursum
            l += 1

        return maxsum
        
