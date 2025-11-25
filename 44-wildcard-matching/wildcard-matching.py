class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        M, N = len(s), len(p)
        dp = [[False] * (M + 1) for _ in range(N + 1)]
        dp[0][0] = True

        for i in range(1, N + 1):
            if p[i - 1] == '*':
                j = 0
                while j < M + 1 and not dp[i - 1][j]:
                    j += 1
                
                if j < M + 1:
                    while j < M + 1:
                        dp[i][j] = True
                        j += 1
            else:
                for j in range(1, M + 1):
                    if dp[i - 1][j - 1] and p[i - 1].isalpha():
                        dp[i][j] = True if p[i - 1] == s[j - 1] else False
                    elif dp[i - 1][j - 1] and p[i - 1] == '?':
                        dp[i][j] = True
        
        return dp[N][M]
