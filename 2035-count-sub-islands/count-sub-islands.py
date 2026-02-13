class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # simultaneous dfs

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid1) or c >= len(grid1[0]) or grid2[r][c] == 0 or (r, c) in visited:
                return True
            visited.add((r,c))
            res = True
            if grid1[r][c] == 0:
                res = False
            
            res = dfs(r+1, c) and res
            res = dfs(r-1, c) and res
            res = dfs(r, c+1) and res
            res = dfs(r, c-1) and res

            return res

        visited = set()
        res = 0
        for r in range(len(grid1)):
            for c in range(len(grid1[0])):
                if grid2[r][c] != 0 and (r, c) not in visited and dfs(r, c):
                    res += 1
        
        return res