class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums = sorted(set(nums))

        l = 0
        r = 1
        cur = 1
        res = 1

        while l < len(nums) and r < len(nums):
            if nums[r] < nums[l] + n:
                r += 1
                cur += 1
            else:
                l += 1
                cur -= 1

            if cur > res:
                res = cur

        res = n - res
        return res