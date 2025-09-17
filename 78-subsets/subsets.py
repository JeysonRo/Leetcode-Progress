class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            for subset in range(len(res)):
                res.append(res[subset] + [i])
                print(res)

        return res