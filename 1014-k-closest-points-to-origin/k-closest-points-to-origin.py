class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] # size k

        distance = [x**2 + y**2 for x,y in points]

        for i in range(len(points)):
            heapq.heappush(heap, (-distance[i], i))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        while heap:
            dist, i = heapq.heappop(heap)
            res.append(points[i])

        return res