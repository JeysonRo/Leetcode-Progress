class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        parents = [[] for i in range(n)]

        for src, to in edges:
            parents[to].append(src)
        
        res = []

        for i, node in enumerate(parents):
            if not node:
                res.append(i)
        
        return res