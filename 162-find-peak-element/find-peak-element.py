class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float("-inf")] + nums + [float("inf")]
        l = 0
        r = len(nums) - 2

        while l < r:
            i = (l + r) // 2
            if nums[i] > nums[i + 1]:  # peak is on left
                r = i
            else:
                l = i + 1
        return l - 1