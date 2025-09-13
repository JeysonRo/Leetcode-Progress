class Solution:
    def findMin(self, nums: List[int]) -> int:
        currentmin = 5000
        l, r = 0, len(nums)

        while l <= r:
            i = (r - l) // 2 + l
            currentmin = min(nums[i], currentmin)
            if nums[i] > nums[-1]: # search right
                l = i + 1
            elif nums[i] <= nums[-1]:
                r = i - 1
        return currentmin