# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, min_num, max_num):
            if not node:
                return True
            left_max = node.val
            left_min = min_num
            right_min = node.val
            right_max = max_num
            if ((not node.left or node.left.val < left_max and node.left.val > left_min) and 
                (not node.right or node.right.val > right_min and node.right.val < right_max)):
                res1 = valid(node.left, left_min, left_max)
                res2 = valid(node.right, right_min, right_max)
            else:
                return False
            
            return res1 and res2
    
        return valid(root, float('-inf'), float('inf'))
