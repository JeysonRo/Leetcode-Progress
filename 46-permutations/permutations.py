class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def recurs(permutation, arr):
            nonlocal res
            for i in range(len(arr)):
                subset = arr[:i] + arr[i+1:]
                recurs(permutation + [arr[i]], subset)
            if len(permutation) == len(nums):
                res.append(permutation)
            return

        recurs([], nums)
        return res