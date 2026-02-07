class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # bfs with bitmask
        goal = 2**len(graph) - 1
        visited = set() # (current node, bitmask)

        queue = deque()
        for i in range(len(graph)):
            queue.appendleft((i, 1 << i))
            visited.add((i, 1 << i))

        res = 0
        while queue:
            for level in range(len(queue)):
                i, bitmask = queue.pop()
                if bitmask == goal:
                    return res
                for neighbor in graph[i]:
                    if (neighbor, bitmask | (1 << neighbor)) not in visited:
                        queue.appendleft((neighbor, bitmask | (1 << neighbor)))
                        visited.add((neighbor, bitmask | (1 << neighbor)))
            res += 1
                
        