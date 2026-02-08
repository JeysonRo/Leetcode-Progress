class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        minheap = []
        for i in nums:
            num = int(i)
            if len(minheap) < k:
                heapq.heappush(minheap, num)
            elif num > minheap[0]:
                heapq.heappop(minheap)
                heapq.heappush(minheap, num)
        
        return str(minheap[0])