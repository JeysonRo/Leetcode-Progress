# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        # return longest side, save largest sum of sides
        def recurs(node):
            nonlocal res
            if not node:
                return 0
            if node.left:
                left = recurs(node.left) + 1
            else:
                left = 0
            if node.right:
                right = recurs(node.right) + 1
            else:
                right = 0
            
            res = max(res, left + right)
            return max(left, right)

        recurs(root)
        return res