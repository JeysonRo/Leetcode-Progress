# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        def recurs(node):
            if not node:
                return node
            if not node.next:
                return node
            child = node.next
            node.next = child.next
            child.next = node
            node.next = recurs(node.next)
            return child

        return recurs(head)

        # [1,2,3,4]
        # node = 3 ->
        # child = 4 -> 3