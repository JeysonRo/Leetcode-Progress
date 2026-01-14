class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        adj = defaultdict(list)

        for src, nei, dist in roads:
            adj[src].append((nei, dist))
            adj[nei].append((src, dist))
        
        visited = set()
        res = adj[1][0][1]

        def dfs(node):
            nonlocal res
            for neighbor, distance in adj[node]:
                if (neighbor, node) not in visited and (node, neighbor) not in visited:
                    visited.add((node, neighbor))
                    res = min(res, distance)
                    dfs(neighbor)

        dfs(1)

        return res