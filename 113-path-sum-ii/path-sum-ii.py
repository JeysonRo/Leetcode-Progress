# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []
        if not root:
            return []
        def dfs(root, cur_sum):
            path.append(root.val)
            cur_sum += root.val
            if not root.left and not root.right:
                if cur_sum == targetSum:
                    res.append(path.copy())
                return
            if root.left:
                dfs(root.left, cur_sum)
                path.pop()
            if root.right:
                dfs(root.right, cur_sum)
                path.pop()
            return
        dfs(root, 0)
        return res