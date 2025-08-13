class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height)-1
        maximum = min(height[p1], height[p2]) * (p2 - p1)

        while p1 < p2:
            if height[p1] <= height[p2]:
                p1 = p1 + 1
                maximum = max(maximum, min(height[p1], height[p2]) * (p2 - p1))

            else:
                p2 = p2 - 1
                maximum = max(maximum, min(height[p1], height[p2]) * (p2 - p1))


        return maximum
