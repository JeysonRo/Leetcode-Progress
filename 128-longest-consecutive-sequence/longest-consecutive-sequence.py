class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxlength = 0
        for i in nums:
            if i - 1 in nums:
                continue
            else:
                length = 0
                while i in nums:
                    length += 1
                    i += 1
                maxlength = max(maxlength, length)
        
        return maxlength