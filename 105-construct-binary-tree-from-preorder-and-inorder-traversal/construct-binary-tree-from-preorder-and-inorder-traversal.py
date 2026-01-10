# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {v : i for i, v in enumerate(inorder)}

        i = 0

        def build(l, r):
            if l > r:
                return None
            
            nonlocal i
            root = TreeNode(preorder[i])
            i += 1

            index = inorder_map[root.val]

            root.left = build(l, index - 1)
            root.right = build(index + 1, r)
            return root

        return build(0, len(inorder) - 1)