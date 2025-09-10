class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        redcount = 0
        whitecount = 0
        bluecount = 0

        for i in nums:
            if i == 0:
                redcount += 1
            if i == 1:
                whitecount += 1
            if i == 2:
                bluecount += 1
        
        for i in range(0, redcount):
            nums[i] = 0
        for i in range(redcount, redcount + whitecount):
            nums[i] = 1
        for i in range(redcount + whitecount, len(nums)):
            nums[i] = 2