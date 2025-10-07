class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = set()
        for i, j in edges:
            nodes.add(i)
            nodes.add(j)
        # print(nodes)
        trees = [set() for i in range(len(nodes)+1)]
        for i in nodes:
            trees[i].add(i)
        # print(trees)

        for node, neighbor in edges:
            for i, tree in enumerate(trees):
                if node in tree:
                    node1 = node
                    node1i = i
                if neighbor in tree:
                    node2 = neighbor
                    node2i = i
            # print(node1i, node1, node2i, node2)
            if node1i == node2i:
                res = [node1, node2]
            elif node1i < node2i:
                trees[node1i].update(trees[node2i])
                trees[node2i] = set()
            else:
                trees[node2i].update(trees[node1i])
                trees[node1i] = set()
            # print(trees)
        
        return res