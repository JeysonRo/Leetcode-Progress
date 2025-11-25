# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        path = set()
        def dfs(node):
            if not node:
                return False
            if node in path:
                return True
            path.add(node)
            res = dfs(node.next)
            path.remove(node)
            return res
        return dfs(head)