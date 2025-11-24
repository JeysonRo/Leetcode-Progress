# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        queue = deque(lists)
        
        while len(queue) >= 2:
            list1 = queue.popleft()
            list2 = queue.popleft()
            if list1 and list2:
                if list1.val <= list2.val:
                    final = ListNode(list1.val)
                    list1 = list1.next
                else:
                    final = ListNode(list2.val)
                    list2 = list2.next
                start = final
                
                while list1 and list2:
                    if list1.val <= list2.val:
                        final.next = ListNode(list1.val)
                        final = final.next
                        list1 = list1.next
                    else:
                        final.next = ListNode(list2.val)
                        final = final.next
                        list2 = list2.next
                if list1:
                    final.next = list1
                if list2:
                    final.next = list2
                
                queue.append(start)
                continue
            if list1:
                queue.appendleft(list1)
            elif list2:
                queue.appendleft(list2)

        if queue:
            return queue.pop()
        return