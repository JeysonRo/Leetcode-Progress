class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find pivot
        l = 0
        r = len(nums) - 1

        while l < r:
            i = l + (r-l) // 2
            if nums[0] > nums[i]:
                r = i
            else:
                l = i + 1
        
        right_partition = r

        # search partitions
        if target >= nums[right_partition] and target <= nums[-1]:
            l = right_partition
            r = len(nums) - 1
        else:
            l = 0
            r = right_partition - 1
        
        #binary search
        while l <= r:
            i = l + (r-l) // 2
            if nums[i] == target:
                return i
            if nums[i] > target:
                r = i - 1
            else:
                l = i + 1
        
        return -1