class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        cache = {}

        def dfs(p1, p2):
            if (p1, p2) in cache:
                return cache[(p1, p2)]
            if p1 >= len(word1) and p2 >= len(word2):
                return 0
            if p2 >= len(word2):
                # only delete
                return len(word1) - p1
            if p1 >= len(word1):
                # only insert
                return len(word2) - p2
            if word1[p1] == word2[p2]:
                cache[(p1, p2)] = dfs(p1+1, p2+1)
            else:
                # 3 decisions
                # insert
                ins = dfs(p1, p2+1) + 1
                # delete
                de = dfs(p1+1, p2) + 1
                # replace
                re = dfs(p1+1, p2+1) + 1
                cache[(p1, p2)] = min(ins, de, re)
            return cache[(p1, p2)]
        
        return dfs(0, 0)