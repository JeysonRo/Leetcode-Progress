# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs, level order
        # right side children first
        # add first node at each level to result array
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            res.append(queue[0].val)
            for i in range(len(queue)):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        
        return res
        