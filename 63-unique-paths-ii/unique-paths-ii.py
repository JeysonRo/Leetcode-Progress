class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        for row in range(ROWS-2, -1, -1):
            for col in range(COLS-2, -1, -1):
                if obstacleGrid[row+1][col] == 1 and obstacleGrid[row][col+1] == 1:
                    obstacleGrid[row][col] = 1
        
        dp = [[0 for j in range(COLS)] for i in range(ROWS)]
        dp[ROWS-1][COLS-1] = 1 if obstacleGrid[ROWS-1][COLS-1] == 0 else 0

        for row in range(ROWS-1, -1, -1):
            for col in range(COLS-1, -1, -1):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                elif row == ROWS-1 and col == COLS-1:
                    dp[row][col] = 1
                elif row == ROWS-1:
                    dp[row][col] = dp[row][col+1]
                elif col == COLS-1:
                    dp[row][col] = dp[row+1][col]
                else:
                    dp[row][col] = dp[row+1][col] + dp[row][col+1]
        
        return dp[0][0]