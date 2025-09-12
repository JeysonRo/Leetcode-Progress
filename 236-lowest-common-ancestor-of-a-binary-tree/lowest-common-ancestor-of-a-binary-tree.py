# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        start = ["b"]

        def dfs(node: 'TreeNode', target: 'TreeNode', path: list = []):
            if node is None:
                return None
            elif node.val == target.val:
                return path + [node]
            
            left = dfs(node.left, target, path + [node])
            right = dfs(node.right, target, path + [node])
            if left is not None:
                return left
            elif right is not None:
                return right
            else:
                return None

        ppath = dfs(root, p)
        qpath = dfs(root, q)
        res = 0
        end = min(len(ppath), len(qpath))
        for i in range(end):
            if ppath[i] == qpath[i]:
                res += 1
            else:
                break
        return ppath[res - 1]