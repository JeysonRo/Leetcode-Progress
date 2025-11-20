class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # bfs

        table = dict()

        for net in times:
            if net[0] not in table:
                table[net[0]] = []
            table[net[0]].append((net[1], net[2]))
        
        visited = set()
        q = []

        heapq.heappush(q, (0, k))
        mintime = 0
        while q:
            node = heapq.heappop(q)
            if node[1] in visited:
                continue
            visited.add(node[1])
            mintime = max(mintime, node[0])
            if node[1] in table:
                for network in table[node[1]]:
                    heapq.heappush(q, (network[1] + node[0], network[0]))
        if len(visited) < n:
            return -1
        return mintime