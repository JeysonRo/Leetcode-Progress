class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        
        adj = defaultdict(list)
        adj[0] = []

        for u,v in edges:
            if u in adj:
                adj[u].append(v)
                adj[v] = adj.get(v, [])
            else:
                adj[v].append(u)
                adj[u] = adj.get(u, [])

        res = 0
        def dfs(node):
            nonlocal res
            path_cost = 0
            min_nodes = 0
            for i, child in enumerate(adj[node]):
                child_path = dfs(child)
                if child_path > path_cost:
                    min_nodes = i
                elif child_path < path_cost:
                    min_nodes += 1
                path_cost = max(path_cost, child_path)

            res += min_nodes
            return path_cost + cost[node]

        dfs(0)
        return res