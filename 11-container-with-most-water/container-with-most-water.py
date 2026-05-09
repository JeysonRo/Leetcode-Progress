class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        largest_area = 0
        l = 0
        r = len(height)-1

        while l < r:
            area = (r - l) * min(height[l], height[r]) 
            largest_area = max(area, largest_area)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return largest_area
