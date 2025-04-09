class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        invnums = [-i for i in nums]
        heapq.heapify(invnums)


        for i in range(k):
            val = heapq.heappop(invnums)
        
        return -val