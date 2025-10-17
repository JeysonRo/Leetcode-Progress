# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pregapNode = None
        gapNode = head
        gap = 1
        cur = head
        while cur.next:
            cur = cur.next
            if gap == n:
                pregapNode = gapNode
                gapNode = gapNode.next
            else:
                gap += 1

        if pregapNode is None:
            return gapNode.next
        pregapNode.next = gapNode.next

        return head