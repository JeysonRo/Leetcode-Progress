# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = root.val
        # return largest side path sum
        def recurs(node):
            nonlocal max_path
            if not node:
                return 0
            
            left = recurs(node.left)
            right = recurs(node.right)

            max_path = max(max_path, node.val, node.val + left, node.val + right, node.val + left + right)

            return max(node.val, left + node.val, right + node.val)

        recurs(root)
        return max_path