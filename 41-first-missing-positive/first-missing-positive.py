class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        i = 1
        while i <= len(nums):
            if i not in nums:
                return i
            i += 1
        return i