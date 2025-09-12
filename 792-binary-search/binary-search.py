class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        res = None
        while l < r:
            index = int(math.floor((r - l) / 2 + l))
            res = nums[index]
            print(l, r, index, res)
            if res == target:
                return index
            elif res > target:
                r = index
            else:
                l = index + 1
        return -1
