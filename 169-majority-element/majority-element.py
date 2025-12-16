class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res = nums[0]
        for i in nums:
            count[i] = count.get(i, 0) + 1
            if count[i] > count[res]:
                res = i
        
        return res