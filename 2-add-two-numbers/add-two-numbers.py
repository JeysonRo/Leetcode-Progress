# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def listToint(head): # convert list into int
            number = 0
            place = 1
            while head:
                number += (head.val * place)
                place *= 10
                head = head.next
            return number

        def intTolist(num): # convert int into list
            if num == 0:
                return ListNode(0, None)
            prev = None
            while num > 0:
                node = ListNode(num % 10, None)
                if prev:
                    prev.next = node
                else:
                    head = node
                num = num // 10
                prev = node
            return head
            
        return intTolist(listToint(l1) + listToint(l2))