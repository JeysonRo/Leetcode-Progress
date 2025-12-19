class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            goal = -nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == goal:
                    res.append([nums[i], nums[j], nums[k]])
                if nums[j] + nums[k] > goal:
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
                else:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
        
        return res