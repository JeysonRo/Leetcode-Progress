# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        heap = []

        queue = deque([root])

        while queue:
            sum_for_level = 0
            for _ in range(len(queue)):
                cur = queue.popleft()
                sum_for_level += cur.val

                if cur.left:
                    queue.append(cur.left)
                
                if cur.right:
                    queue.append(cur.right)

            heapq.heappush(heap, sum_for_level)

            if len(heap) > k:
                heapq.heappop(heap)

        if len(heap) < k:
            return -1

        return heap[0]
