# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = 0
        res = root.val
        def recurs(node):
            nonlocal count
            nonlocal res
            if not node:
                return
            recurs(node.left)
            count += 1
            if count == k:
                res = node.val
                return
            else:
                recurs(node.right)
            return
        
        recurs(root)
        return res