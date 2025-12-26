class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        dp = grid

        for row in range(ROWS):
            for col in range(COLS):
                if row == 0 and col == 0:
                    dp[row][col] = grid[row][col]
                    continue
                up = dp[row-1][col] if row != 0 else sys.maxsize
                left = dp[row][col-1] if col != 0 else sys.maxsize
                dp[row][col] = grid[row][col] + min(up, left)

        return dp[ROWS-1][COLS-1]