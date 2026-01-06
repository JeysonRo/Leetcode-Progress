class UnionFind:
    # path compression + union by rank
    def __init__(self, nodes: int):
        self.parent = [i for i in range(nodes)]
        self.rank = [1 for i in range(nodes)]
    
    def find(self, node: int):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node]) # path compression (compress each node in chain to root parent)
        return self.parent[node]

    def union(self, nodea: int, nodeb: int):
        roota = self.find(nodea)
        rootb = self.find(nodeb)

        if roota != rootb:
            if self.rank[roota] == self.rank[rootb]:
                self.rank[roota] += 1
                self.parent[rootb] = roota
            elif self.rank[roota] < self.rank[rootb]:
                self.parent[roota] = rootb
            else:
                self.parent[rootb] = roota
            return True
        else: 
            return False

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        adj = [[] for i in range(len(vals))]
        for src, nei in edges:
            adj[src].append(nei)
            adj[nei].append(src)
        
        valtoindex = defaultdict(list)
        for i, val in enumerate(vals):
            valtoindex[val].append(i)

        unionfind = UnionFind(len(vals))
        res = 0
        for val in sorted(valtoindex.keys()):
            for i in valtoindex[val]:
                for nei in adj[i]:
                    if vals[nei] <= vals[i]:
                        unionfind.union(i, nei)
            count = defaultdict(int)
            for i in valtoindex[val]:
                count[unionfind.find(i)] += 1
                res += count[unionfind.find(i)]

        return res