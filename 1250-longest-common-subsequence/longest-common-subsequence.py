class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROW = len(text1)
        COL = len(text2)
        dp = {} # key (i, j) : value lcs of text up to that length

        for i in range(ROW):
            for j in range(COL):
                dp[(i, j)] = 0

        for i in range(ROW):
            for j in range(COL):
                if text1[i] == text2[j]:
                    if (i-1,j) in dp and (i,j-1) in dp:
                        dp[(i,j)] = 1 + dp[(i-1,j-1)]
                    else:
                        dp[(i,j)] = 1
                else:
                    dp[(i, j)] = max(dp[(i, j-1)] if (i,j-1) in dp else 0, dp[(i-1,j)] if (i-1,j) in dp else 0)

        return dp[(ROW-1,COL-1)]