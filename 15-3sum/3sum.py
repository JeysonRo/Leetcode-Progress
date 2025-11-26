class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        print(nums)
        res = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == num:
                continue
            j = i + 1
            k = len(nums) - 1
            target = -num
            while j < k:
                if k < len(nums) - 1 and nums[k] == nums[k+1]:
                    k -= 1
                    continue
                if j > i + 1 and nums[j] == nums[j-1]:
                    j += 1
                    continue
                res_sum = nums[j] + nums[k]
                if res_sum == target:
                    res.append([nums[i],nums[j],nums[k]])
                    k -= 1
                    j += 1
                elif res_sum > target:
                    k -= 1
                elif res_sum < target:
                    j += 1
            
        return res