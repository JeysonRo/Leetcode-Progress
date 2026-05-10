"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # bfs

        table = {} # original node : copy node
        
        def dfs(node):
            if not node:
                return None
            
            if node not in table:
                # create copy, add to table
                node_copy = Node(node.val)
                table[node] = node_copy
            
                if node.neighbors:
                    node_copy.neighbors = []
                    for neighbor in node.neighbors:
                        node_copy.neighbors.append(dfs(neighbor))
            
            else:
                node_copy = table[node]
            
            return node_copy
        
        return dfs(node)