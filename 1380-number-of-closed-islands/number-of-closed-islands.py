class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        # dfs

        visited = set()
        res = 0
        directions = ((0,1), (1,0), (0,-1), (-1,0))

        def dfs(row, col):
            if row < 0 or row == M or col < 0 or col == N:
                return 0
            if grid[row][col] == 1:
                return 1
            if (row, col) in visited:
                return 1
            visited.add((row, col))
            res = 0
            res = (min(dfs(row+1, col), 
                dfs(row-1, col), 
                dfs(row, col+1), 
                dfs(row, col-1)))
            return res

        for row in range(M):
            for col in range(N):
                if grid[row][col] == 0 and (row, col) not in visited:
                    res += dfs(row, col)
        
        return res