class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        area = 0

        def dfs(m, n) -> int:
            if (m, n) in visited:
                return 0
            visited.add((m,n))
            if m < 0 or n < 0 or m >= rows or n >= cols or grid[m][n] == 0:
                return 0
            area = 1
            area += dfs(m+1,n)
            area += dfs(m-1,n)
            area += dfs(m,n+1)
            area += dfs(m,n-1)
            print("area is: ", area)
            return area


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = max(area, dfs(row, col))
        
        return area
