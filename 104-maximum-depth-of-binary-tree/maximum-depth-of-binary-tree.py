# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0
            
            left_len = dfs(root.left) + 1
            right_len = dfs(root.right) + 1
            return max(left_len, right_len)
        
        return dfs(root)