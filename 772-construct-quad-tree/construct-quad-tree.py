"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def sameLeaf(topLeft, topRight, bottomLeft, bottomRight):
            return (topLeft.isLeaf and 
                    topRight.isLeaf and 
                    bottomLeft.isLeaf and 
                    bottomRight.isLeaf and 
                    topLeft.val == topRight.val and 
                    topRight.val == bottomLeft.val and 
                    bottomLeft.val == bottomRight.val)

        def createNode(x, y, width):
            if width == 1:
                return Node(grid[x][y] == 1, True, None, None, None, None)
            val = True
            isLeaf = False
            topLeft = createNode(x, y, width // 2)
            topRight = createNode(x, y + width // 2, width // 2)
            bottomLeft = createNode(x + width // 2, y, width // 2)
            bottomRight = createNode(x + width // 2, y + width // 2, width // 2)
            if sameLeaf(topLeft, topRight, bottomLeft, bottomRight):
                val = topLeft.val
                return Node(val, True, None, None, None, None)
            
            return Node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight)
        
        return createNode(0, 0, len(grid))