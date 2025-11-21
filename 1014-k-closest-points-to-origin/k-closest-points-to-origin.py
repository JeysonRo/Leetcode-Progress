class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []

        for x,y in points:
            minheap.append((x**2 + y**2, x, y))
        heapq.heapify(minheap)

        res = []

        for i in range(k):
            d, x, y = heapq.heappop(minheap)
            res.append([x, y])
        
        return res