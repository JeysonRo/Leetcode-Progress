class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = set()
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            remainder = cur_sum % k
            if remainder in remainders:
                return True
            if i-1 >= 0:
                remainders.add(prev)
            if 0 not in remainders:
                remainders.add(0)
            prev = remainder
        
        return False