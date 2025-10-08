class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        grid = [[0] * n] * m

        grid[0][0] = 1

        for row in range(m):
            for col in range(n):
                if col == 0 or row == 0:
                    grid[row][col] = 1
                else:
                    grid[row][col] = grid[row-1][col] + grid[row][col-1]


        return grid[m-1][n-1]