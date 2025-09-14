# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []

        q.appendleft(root)

        while q:
            count = len(q)
            found = False
            for i in range(count):
                node = q.popleft()
                if node:
                    if not found:
                        found = True
                        res.append(node.val)
                    q.append(node.right)
                    q.append(node.left)
        return res
                        

                