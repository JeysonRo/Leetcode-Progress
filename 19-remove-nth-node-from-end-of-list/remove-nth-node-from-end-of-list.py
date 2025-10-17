# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pregapNode = head
        gap = 0
        cur = head
        while cur.next:
            cur = cur.next
            if gap == n:
                pregapNode = pregapNode.next
            else:
                gap += 1

        if gap != n:
            return head.next
        print(pregapNode.val)
        pregapNode.next = pregapNode.next.next

        return head