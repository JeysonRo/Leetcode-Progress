# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n > 1 and n % 2 == 0:
            return []
        res = []

        def build(n):
            if n == 0:
                return []
            if n == 1:
                return [TreeNode()]
            
            res = []
            for l in range(1, n, 2): 
                r = n - 1 - l
                leftTrees, rightTrees = build(l), build(r)

                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0, t1, t2))
            return res
        
        return build(n)