class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            i = (l + r) // 2

            if i % 2 == 0: # even
                if nums[i] == nums[i+1]: # on the left of the single element
                    l = i + 2
                else: # on the right of the single element
                    r = i
            else: # odd
                if nums[i] == nums[i-1]: # on the left
                    l = i + 1
                else:
                    r = i - 1
        
        return nums[r]
            
