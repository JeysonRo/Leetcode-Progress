# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # empty list

        l = 0
        r = len(nums) - 1

        def recurs(l, r):
            if l > r:
                return None
            i = l + (r - l) // 2
            node = TreeNode(nums[i])
            node.left = (recurs(l,i - 1))
            node.right = (recurs(i + 1,r))
            return node
        
        return recurs(l, r)