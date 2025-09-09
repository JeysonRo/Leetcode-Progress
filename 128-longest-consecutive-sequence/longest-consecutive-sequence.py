class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        bank = set(nums)
        maximum = 1
        count = 1
        for i in bank:
            if i - 1 not in bank:
                val = i
                while val + 1 in bank:
                    count += 1
                    val += 1
                maximum = max(maximum, count)
                count = 1
        return maximum
