# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height_balanced = True
        def recurs(root):
            nonlocal height_balanced
            if root is None:
                return -1
            left_height = 1 + recurs(root.left)
            right_height = 1 + recurs(root.right)
            if abs(right_height - left_height) > 1:
                height_balanced = False
            return max(left_height, right_height)
        
        recurs(root)
        return height_balanced