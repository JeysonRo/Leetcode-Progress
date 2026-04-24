class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recurs(cur_set, i):
            # decide, keep or skip element
            if i >= len(nums):
                res.append(cur_set)
                return
            recurs(cur_set, i+1)
            recurs(cur_set + [nums[i]], i+1)
            return

        recurs([], 0)

        return res