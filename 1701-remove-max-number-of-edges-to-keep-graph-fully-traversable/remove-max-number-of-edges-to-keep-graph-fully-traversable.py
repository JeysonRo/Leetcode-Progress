class UnionFind:
    def __init__(self, n:int):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    
    def union(self, nodeA, nodeB):
        parentA = self.find(nodeA)
        parentB = self.find(nodeB)
        if parentA == parentB:
            return False
        if self.size[parentA] >= self.size[parentB]:
            self.parent[parentB] = parentA
            self.size[parentA] += self.size[parentB]
        else:
            self.parent[parentA] = parentB
            self.size[parentB] += self.size[parentA]
        return True
    
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def copy(self):
        new_copy = UnionFind(len(self.parent))
        new_copy.parent = self.parent.copy()
        new_copy.size = self.size.copy()
        return new_copy

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # unionfind
        og = UnionFind(n+1) # type 3
        res = 0
        for etype, node1, node2 in edges:
            if etype == 3:
                parent1 = og.find(node1)
                parent2 = og.find(node2)
                if parent1 == parent2:
                    res += 1
                og.union(parent1, parent2)

        Alice = og.copy()
        Bob = og.copy()
        for etype, node1, node2 in edges:
            remove = False
            if etype == 1:
                parent1 = Alice.find(node1)
                parent2 = Alice.find(node2)
                if parent1 == parent2:
                    remove = True
                Alice.union(parent1, parent2)
            if etype == 2:
                parent1 = Bob.find(node1)
                parent2 = Bob.find(node2)
                if parent1 == parent2:
                    remove = True
                Bob.union(parent1, parent2)
            if remove:
                res += 1

        for i in range(1,n+1):
            if Alice.find(i) != Alice.find(1) or Bob.find(i) != Bob.find(1):
                return -1
        return res