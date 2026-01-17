class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i == j:
                return 1
            if i > j:
                return 0
            if s[i] == s[j]:
                length = 2
                return length + dfs(i + 1, j - 1)
            else:
                return max(dfs(i + 1, j), dfs(i, j - 1))
        
        return dfs(0, len(s) - 1)