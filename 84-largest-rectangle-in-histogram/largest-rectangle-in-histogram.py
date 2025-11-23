class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [] # (height, index)  strictly increasing
        maxarea = heights[0]

        for i, height in enumerate(heights):
            if not stack:
                stack.append((height, i))
            elif height >= stack[-1][0]:
                stack.append((height, i))
            else:
                while stack and stack[-1][0] > height:
                    blockheight, index = stack.pop()
                    maxarea = max(maxarea, (blockheight * (i - index)))
                stack.append((height, index))
        
        while stack:
                blockheight, index = stack.pop()
                maxarea = max(maxarea, (blockheight * (len(heights) - index)))

        return maxarea