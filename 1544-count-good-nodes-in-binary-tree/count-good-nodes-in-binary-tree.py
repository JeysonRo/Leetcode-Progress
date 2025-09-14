# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        maxval = -10**4
        def countGood(node, maxval):
            good = 0
            if node:
                if node.val >= maxval:
                    good += 1
                maxval = max(maxval, node.val)
                good += countGood(node.left, maxval)
                good += countGood(node.right, maxval)
            return good

        return countGood(root, maxval)