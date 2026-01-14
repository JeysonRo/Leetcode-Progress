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
                return False
            if grid[row][col] == 1:
                return True
            if (row, col) in visited:
                return False
            visited.add((row, col))
            res = True
            for direction in directions:
                next_row, next_col = row + direction[0], col + direction[1]
                if (next_row, next_col) not in visited:
                    val = dfs(next_row, next_col)
                    res = res and val
            return res

        for row in range(M):
            for col in range(N):
                if grid[row][col] == 0 and (row, col) not in visited:
                    if dfs(row, col):
                        res += 1
        
        return res