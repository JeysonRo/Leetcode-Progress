class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []

        for i in range(len(nums)):
            if nums[i] == key:
                for j in range(i-k, i+k+1):
                    if j < 0 or j >= len(nums) or len(res) > 0 and res[-1] >= j:
                        continue
                    res.append(j)
        
        return res