class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        # multi - source bfs

        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        queue = deque()
        visited = set()

        answer = False
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    queue.appendleft((i,j))
                    visited.add((i,j))
                else:
                    answer = True
        if not answer:
            return -1

        cur_distance = -1
        while queue:
            cur_distance += 1
            for _ in range(len(queue)):
                i, j = queue.pop()
                for dir in directions:
                    if (dir[0] + i >= 0 and dir[0] + i < N 
                    and dir[1] + j >= 0 and dir[1] + j < N
                    and (dir[0] + i, dir[1] + j) not in visited):
                        queue.appendleft((dir[0] + i, dir[1] + j))
                        visited.add((dir[0] + i, dir[1] + j))
        
        return cur_distance