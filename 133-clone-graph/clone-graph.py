# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []
# """

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = set()

        def dfs(curnode):
            if curnode in visited:
                return
            visited.add(curnode)
            for i in curnode.neighbors:
                dfs(i)
    
        newnode = copy.deepcopy(node)

        return newnode