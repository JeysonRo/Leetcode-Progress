class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # prefix sum

        cur_sum = 0
        table = set()
        prev_remainder = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            sum_remainder = cur_sum % k
            if sum_remainder in table:
                return True

            table.add(prev_remainder)
            prev_remainder = sum_remainder
        
        return False