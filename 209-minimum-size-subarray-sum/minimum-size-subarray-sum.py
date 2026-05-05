class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # target > 0
        # len(nums) > 0

        l = 0
        r = 0
        cur_sum = nums[0]
        min_len = float('inf')
        while r < len(nums):
            # sum >= target
            if cur_sum >= target:
                min_len = min(min_len, r - l + 1)
                cur_sum -= nums[l]
                l += 1
            # sum < target
            else:
                r += 1
                if r < len(nums):
                    cur_sum += nums[r]
        
        if min_len == float('inf'):
            return 0
        return min_len

        # time: O(n) n is length of array
        # space: O(1)
                                  