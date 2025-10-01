class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        def dfs(m, n):
            if (m, n) in visited:
                return
            visited.add((m, n))
            # traverse every direction for land
            if m >= 0 and n >= 0 and m < rows and n < cols and grid[m][n] == "1":
                dfs(m + 1, n) # down
                dfs(m - 1, n) # up
                dfs(m, n + 1) # right
                dfs(m, n - 1) # left
            

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
            
        return res