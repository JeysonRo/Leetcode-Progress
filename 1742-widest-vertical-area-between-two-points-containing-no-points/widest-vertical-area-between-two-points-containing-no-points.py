class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        points.sort()
        maxarea = points[1][0] - points[0][0]
        for i in range(0, len(points)-1):
            width = points[i+1][0] - points[i][0]
            if width > maxarea:
                maxarea = width
        
        return maxarea