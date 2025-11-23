class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        bank = set(nums)
        maxlen = 0
        
        for i in bank:
            if i - 1 in bank:
                continue
            curlen = 1
            while i + 1 in bank:
                i += 1
                curlen += 1
            maxlen = max(maxlen, curlen)
        
        return maxlen