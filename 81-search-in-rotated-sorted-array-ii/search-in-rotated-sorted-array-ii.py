class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # find pivot

        l = 0
        r = len(nums) - 1

        while l <= r:
            i = l + (r-l) // 2
            if nums[i] == target:
                return True

            if nums[l] < nums[i]: # left partition
                if nums[l] <= target and target < nums[i]:
                    r = i - 1
                else:
                    l = i + 1

            elif nums[l] > nums[i]: # right partition
                if nums[i] < target and target <= nums[r]:
                    l = i + 1
                else:
                    r = i - 1
            else:
                l += 1
        
        return False
