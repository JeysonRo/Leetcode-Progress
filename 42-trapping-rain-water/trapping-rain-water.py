class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = 0
        res = 0
        buffer = 0
        while r < len(height):
            if height[r] >= height[l]:
                l = r
                res += buffer
                buffer = 0
            elif height[r] < height[l]:
                buffer += height[l] - height[r]
            r += 1
        
        stop = l
        l = r = len(height) - 1
        buffer = 0
        while l >= stop:
            if height[l] >= height[r]:
                r = l
                res += buffer
                buffer = 0
            else:
                buffer += height[r] - height[l]
            l -= 1
        
        return res