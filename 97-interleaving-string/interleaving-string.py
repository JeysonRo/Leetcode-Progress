class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        p1 = p2 = 0

        cache = {} # cache[i, p1, p2] = True or False

        def dfs(i, p1, p2):
            if (i, p1, p2) in cache:
                return cache[(i, p1, p2)]
            res1 = res2 = False
            if p1 >= len(s1) and p2 >= len(s2):
                return True
            if p1 < len(s1):
                if s1[p1] == s3[i]:
                    cache[i+1, p1+1, p2] = dfs(i+1, p1+1, p2)
                    res1 = cache[i+1, p1+1, p2]
            if p2 < len(s2):
                if s2[p2] == s3[i]:
                    cache[i+1, p1, p2+1] = dfs(i+1, p1, p2+1)
                    res2 = cache[i+1, p1, p2+1]
            return res1 or res2
        
        return dfs(0, 0, 0)