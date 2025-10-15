# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        def recurs(prev, node):
            if node.next is None:
                node.next = prev
                return node
            final = recurs(node, node.next)
            node.next = prev
            return final

        return recurs(None, head)