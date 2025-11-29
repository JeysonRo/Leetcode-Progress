class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        cur = 0
        k_use = 0
        max1 = 0
        while r < len(nums):
            if l > r:
                r += 1
                continue
            if nums[r] == 1:
                cur += 1
                max1 = max(max1,cur)
                r += 1
            elif k > k_use:
                k_use += 1
                cur += 1
                max1 = max(max1,cur)
                r += 1
            else:
                if nums[l] == 1:
                    cur -= 1
                elif nums[l] == 0 and k_use > 0:
                    k_use -= 1
                    cur -= 1                
                l += 1
        max1 = max(max1, cur)
        return max1
'''
 0,1,2,3,4,5,6,7,8,9,10
   l               r
[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1] k_use = 3 k = 3
'''