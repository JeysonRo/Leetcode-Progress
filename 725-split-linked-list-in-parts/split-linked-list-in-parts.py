# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if k == 1:
            return [head]
        # find len
        length = 0
        cur = head
        while cur is not None:
            length += 1
            cur = cur.next
        
        group_size = int(math.ceil(length / k))
        longer_groups = length % k

        res = [None for i in range(k)]
        cur = head
        i = 0
        while i < longer_groups or (i < k and longer_groups == 0):
            res[i] = cur
            for j in range(1, group_size):
                cur = cur.next
            prev = cur
            if cur:
                cur = cur.next
            if prev:
                prev.next = None
            i += 1
        
        while i < k:
            res[i] = cur
            for j in range(1, group_size-1):
                cur = cur.next
            prev = cur
            if cur:
                cur = cur.next
            if prev:
                prev.next = None
            i += 1
        
        return res