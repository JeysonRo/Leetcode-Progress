class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        farthest = 0

        p = 0
        while p < goal:
            if nums[p] == 0:
                while p > 0:
                    p -= 1
                    if p + nums[p] > farthest:
                        farthest = p = p + nums[p]
                        break
                if p == 0:
                    return False
            if p >= goal:
                return True
            p += nums[p]
            farthest = max(farthest, p)
        if farthest >= goal:
            return True
        else:
            print("idk lol")
            return False