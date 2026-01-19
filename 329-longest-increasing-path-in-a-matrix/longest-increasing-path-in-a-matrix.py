class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M = len(matrix)
        N = len(matrix[0])

        @lru_cache(None)
        def dfs(row, col):
            res = []
            val = matrix[row][col]
            if row + 1 < M and matrix[row + 1][col] > val:
                res.append(dfs(row+1, col))
            if row - 1 >= 0 and matrix[row - 1][col] > val:
                res.append(dfs(row-1, col))
            if col + 1 < N and matrix[row][col + 1] > val:
                res.append(dfs(row, col+1))
            if col - 1 >= 0 and matrix[row][col - 1] > val:
                res.append(dfs(row, col-1))
            if len(res) == 0:
                return 1
            else:
                return 1 + max(res)

        res = 0
        for row in range(M):
            for col in range(N):
                cur = dfs(row, col)
                res = max(cur, res)

        return res