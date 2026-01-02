class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        heap = []
        visited = set()

        adj = defaultdict(list) # node : list(neighbor, weight)

        for i, edge in enumerate(edges):
            a = edge[0]
            b = edge[1]
            adj[a].append((b, succProb[i]))
            adj[b].append((a, succProb[i]))
        
        heapq.heappush(heap, (-1, start_node))

        while heap:
            prob, node = heapq.heappop(heap)
            prob = -prob
            if node == end_node:
                return prob
            if node in visited:
                continue
            visited.add(node)
            for neighbor, neighbor_prob in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (-prob*neighbor_prob, neighbor))

        return 0                