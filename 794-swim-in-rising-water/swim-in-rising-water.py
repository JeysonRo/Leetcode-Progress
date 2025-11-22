class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        start = (0, 0)
        goal = (N-1, N-1)
        
        Minheap = [] # (height, (coordinate))
        visited = set()
        Minheight = 0

        # traverse from start
        heapq.heappush(Minheap, (grid[0][0], 0, 0))

        while Minheap:
            height, x, y = heapq.heappop(Minheap)
            if (x,y) in visited:
                continue
            visited.add((x,y))
            Minheight = max(Minheight, height)
            if (x,y) == goal:
                return Minheight
            # push 4 cardinal directions into heap
            if x > 0 and (x-1,y) not in visited:
                heapq.heappush(Minheap, (grid[x-1][y], x-1, y))
            if x < N-1 and (x+1,y) not in visited:
                heapq.heappush(Minheap, (grid[x+1][y], x+1, y))
            if y > 0 and (x,y-1) not in visited:
                heapq.heappush(Minheap, (grid[x][y-1], x, y-1))
            if y < N-1 and (x,y+1) not in visited:
                heapq.heappush(Minheap, (grid[x][y+1], x, y+1))
            