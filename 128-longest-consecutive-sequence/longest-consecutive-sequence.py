class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        bank = set(nums)
        maxlen = 0

        for i in bank:
            if i-1 not in bank:
                length = 0
                while (i + length) in bank:
                    length += 1
                maxlen = max(length, maxlen)
        return maxlen