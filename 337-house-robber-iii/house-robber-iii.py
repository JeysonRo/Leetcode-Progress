# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # dfs
        # 4 options, return maximum
        # root + left grandchild + right grandchild
        # left child + right child
        # left grandchild + right child
        # left child + right grandchild
        @cache
        def dfs(root):
            if not root:
                return 0
                
            left_grandchild = dfs(root.left.left) + dfs(root.left.right) if root.left else 0
            right_grandchild = dfs(root.right.left) + dfs(root.right.right) if root.right else 0
            left_child = dfs(root.left)
            right_child = dfs(root.right)

            res = []
            res.append(root.val + left_grandchild + right_grandchild)
            res.append(left_child + right_child)
            res.append(left_grandchild + right_child)
            res.append(left_child + right_grandchild)
            return max(res)
        
        return dfs(root)