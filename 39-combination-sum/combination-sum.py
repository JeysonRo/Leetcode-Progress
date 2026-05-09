class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # decision tree

        # add current number to sum
        # increment i to next number
        res = []
        combination = []
        def recurs(i, cur_sum):
            if i >= len(candidates):
                return
            if cur_sum == target:
                res.append(combination.copy())
                return
            if cur_sum > target:
                return
            
            combination.append(candidates[i])
            recurs(i, cur_sum + candidates[i])
            combination.pop()

            recurs(i+1, cur_sum)
        
        recurs(0, 0)
        return res
