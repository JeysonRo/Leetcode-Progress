class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # find rotation
        while l <= r:
            i = (r - l) // 2 + l

            if nums[i] == target:
                return i
            elif nums[i] > nums[-1]:
                l = i + 1
            elif nums[i] <= nums[-1]:
                r = i - 1
        split = i
        #search left
        l = 0
        r = split - 1
        while l <= r:
            i = (r - l) // 2 + l

            if nums[i] == target:
                return i
            elif nums[i] > target:
                r = i - 1
            elif nums[i] < target:
                l = i + 1

        #search right
        l = split + 1
        r = len(nums) - 1
        while l <= r:
            i = (r - l) // 2 + l

            if nums[i] == target:
                return i
            elif nums[i] > target:
                r = i - 1
            elif nums[i] < target:
                l = i + 1

        return -1
            