class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # bfs
        m = len(grid)
        n = len(grid[0])
        goal = (m-1,n-1)
        visited = set() # (m, n, k)
        steps = -1

        queue = deque()
        queue.appendleft((0,0,k))
        while queue:
            steps += 1
            for i in range(len(queue)):
                x, y, k = queue.pop()
                if (x,y,k) in visited:
                    continue
                visited.add((x,y,k))

                if (x,y) == goal:
                    return steps

                if x > 0:
                    if grid[x-1][y] == 1 and k > 0:
                        queue.appendleft((x-1,y,k-1))
                    elif grid[x-1][y] == 0:
                        queue.appendleft((x-1,y,k))
                if y > 0:
                    if grid[x][y-1] == 1 and k > 0:
                        queue.appendleft((x,y-1,k-1))
                    elif grid[x][y-1] == 0:
                        queue.appendleft((x,y-1,k))
                if x < m - 1:
                    if grid[x+1][y] == 1 and k > 0:
                        queue.appendleft((x+1,y,k-1))
                    elif grid[x+1][y] == 0:
                        queue.appendleft((x+1,y,k))
                if y < n - 1:
                    if grid[x][y+1] == 1 and k > 0:
                        queue.appendleft((x,y+1,k-1))
                    elif grid[x][y+1] == 0:
                        queue.appendleft((x,y+1,k))
                
        
        return -1