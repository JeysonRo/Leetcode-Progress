class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        directions = [(-1,0), (1,0), (0, 1), (0,-1)]
        cells = [[0 for i in grid] for j in grid]
        queue = deque()
        visited = set() # (r,c)
        for r, rv in enumerate(grid):
            for c,cv in enumerate(rv):
                if cv == 1:
                    queue.appendleft((r,c))
                    visited.add((r,c))

        distance = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.pop()
                cells[r][c] = distance

                for j in directions:
                    if r + j[0] >= 0 and r + j[0] < len(cells) and c + j[1] >= 0 and c + j[1] < len(cells) and (r + j[0], c + j[1]) not in visited:
                        queue.appendleft((r + j[0], c + j[1]))
                        visited.add((r + j[0], c + j[1]))
            distance += 1

        print(cells)

        goal = (len(cells) - 1, len(cells) - 1)
        pqueue = [] # (safeness, r, c)
        visited = set()
        heapq.heappush(pqueue, (-cells[0][0], 0, 0))
        while pqueue:
            safeness, r, c = heapq.heappop(pqueue)
            safeness = -safeness
            res = safeness
            if res == 0 or (r,c) == goal:
                return res
            for j in directions:
                if r + j[0] >= 0 and r + j[0] < len(cells) and c + j[1] >= 0 and c + j[1] < len(cells) and (r + j[0], c + j[1]) not in visited:
                    heapq.heappush(pqueue, (-min(safeness, cells[r+j[0]][c+j[1]]), r + j[0], c + j[1]))
                    visited.add((r + j[0], c + j[1]))

        return res