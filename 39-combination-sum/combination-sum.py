class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def combination(i, path, target):
            if i >= len(candidates):
                return
            if target > 0:

                combination(i, path + [candidates[i]], target - candidates[i])

                combination(i+1, path, target)
            elif target == 0:
                res.append(path.copy())
            return
        
        combination(0, path, target)
        return res