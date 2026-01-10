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

        def createNode(r, c, width):
            sameLeaf = True
            for i in range(r, r + width):
                for j in range(c, c + width):
                    if grid[i][j] != grid[r][c]:
                        sameLeaf = False
                        break
                if not sameLeaf:
                    break

            if sameLeaf:
                val = grid[i][j]
                return Node(val, True)

            val = True
            isLeaf = False
            topLeft = createNode(r, c, width // 2)
            topRight = createNode(r, c + width // 2, width // 2)
            bottomLeft = createNode(r + width // 2, c, width // 2)
            bottomRight = createNode(r + width // 2, c + width // 2, width // 2)
            
            return Node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight)
        
        return createNode(0, 0, len(grid))