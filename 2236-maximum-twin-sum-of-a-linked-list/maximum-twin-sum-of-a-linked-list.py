# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        newlist = []

        while head is not None:
            newlist.append(head.val)
            head = head.next

        l = 0
        r = len(newlist) - 1
        res = newlist[l] + newlist[r]

        while l < r:
            res = max(res, newlist[l] + newlist[r])
            l += 1
            r -= 1
        
        return res