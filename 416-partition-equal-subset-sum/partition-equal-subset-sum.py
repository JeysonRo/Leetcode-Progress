class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # find a subset whose sum is equal to exactly half of the sum of the original set
        # if found then return true
        
        # decision tree decisions at every index

        # include element in subset
        # skip element

        target = sum(nums)
        if target % 2 == 1:
            return False
        target = target // 2

        @cache
        def recurs(i, cur_sum):
            if cur_sum == target:
                return True
            if cur_sum > target:
                return False
            if i >= len(nums):
                return False
            #cache

            res1 = recurs(i+1, cur_sum+nums[i])
            if res1:
                return True
            return recurs(i+1, cur_sum)

        return recurs(0, 0)