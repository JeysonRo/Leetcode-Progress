# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #dfs
        highest_maxsum = float("-inf")
        def dfs(root):
            if not root:
                return 0
            nonlocal highest_maxsum
            maxsum = root.val
            leftsum = dfs(root.left)
            rightsum = dfs(root.right)
            if root.val + leftsum > maxsum:
                maxsum = root.val + leftsum
            if root.val + rightsum > maxsum:
                maxsum = root.val + rightsum
            highest_maxsum = max(highest_maxsum, maxsum, root.val + leftsum + rightsum)
            return maxsum

        dfs(root)

        return highest_maxsum