# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(root, cur):
            if root.left and root.right:
                return dfs(root.left, cur + root.val) or dfs(root.right, cur + root.val)
            if root.left:
                return dfs(root.left, cur + root.val)
            if root.right:
                return dfs(root.right, cur + root.val)
            return cur + root.val == targetSum
        return dfs(root, 0)