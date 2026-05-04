class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        

    def addNum(self, num: int) -> None: # O(logn) 
        heapq.heappush(self.minheap, num)
        val = heapq.heappop(self.minheap)
        heapq.heappush(self.maxheap, -val)
        val = heapq.heappop(self.maxheap)
        heapq.heappush(self.minheap, -val)
        while len(self.minheap) - len(self.maxheap) > 1:
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -val)


    def findMedian(self) -> float: # O(1)
        # even
        if (len(self.minheap) + len(self.maxheap)) % 2 == 0:
            return (self.minheap[0] - self.maxheap[0]) / 2
        else: # odd
            return self.minheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()