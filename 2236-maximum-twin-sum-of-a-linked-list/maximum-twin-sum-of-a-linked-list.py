# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        def reverse(head):
            prev = None
            cur = head
            next = head.next

            while cur:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            return

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        reverse(slow.next)
        l = head
        r = fast
        res = l.val + r.val

        while l and r:
            res = max(res, l.val + r.val)
            l = l.next
            r = r.next
        
        return res