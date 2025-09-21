class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        res.add(())
        new = []
        for val in nums:
            res.update(new)
            for subset in res:
                if subset + (val,) not in res:
                    new.append(subset + (val,))
        res.update(new)
        
        return list(res)