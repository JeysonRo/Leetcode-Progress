# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, minval, maxval):
            if root is None:
                return True
            if root.val >= maxval or root.val <= minval:
                return False
            
            left = valid(root.left, minval, root.val)
            right = valid(root.right, root.val, maxval)

            return left and right

        return valid(root, -sys.maxsize, sys.maxsize)