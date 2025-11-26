class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def combination(i, target):
            if i >= len(candidates):
                return
            if target > 0:
                path.append(candidates[i])
                combination(i, target - candidates[i])
                path.pop()
                combination(i+1, target)
            elif target == 0:
                res.append(path.copy())
            return
        
        combination(0, target)
        return res