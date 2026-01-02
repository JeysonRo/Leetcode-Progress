class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        
        dp = [0 for j in range(COLS)]

        for row in range(ROWS-1, -1, -1):
            for col in range(COLS-1, -1, -1):
                if obstacleGrid[row][col] == 1:
                    dp[col] = 0
                elif row == ROWS-1 and col == COLS-1:
                    dp[col] = 1
                elif row == ROWS-1:
                    dp[col] = dp[col+1]
                elif col == COLS-1:
                    continue
                    # dp[col] = dp[col]
                else:
                    dp[col] = dp[col] + dp[col+1]
        
        return dp[0]