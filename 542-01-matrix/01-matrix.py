class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # multi source bfs
        M = len(mat)
        N = len(mat[0])
        res = [[0 for i in range(N)] for j in range(M)]
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        queue = deque()
        visited = set() # (m,n)

        for i in range(M):
            for j in range(N):
                if mat[i][j] == 0:
                    queue.appendleft((i,j))
                    visited.add((i,j))
        
        distance = 0

        while queue:
            for i in range(len(queue)):
                x,y = queue.pop()
                res[x][y] = distance

                for dire in directions:
                    if x+dire[0] >= 0 and x+dire[0] < M and y+dire[1] >= 0 and y+dire[1] < N and (x+dire[0],y+dire[1]) not in visited:
                        queue.appendleft((x+dire[0],y+dire[1]))
                        visited.add((x+dire[0],y+dire[1]))
            distance += 1
        
        return res