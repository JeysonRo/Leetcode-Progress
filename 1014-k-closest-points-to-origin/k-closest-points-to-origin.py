class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []

        for x, y in points:
            val = (x**2 + y**2)
            distance.append([val, x, y])
        heapq.heapify(distance)
        
        res = []
        while k > 0:
            k -= 1
            val,x,y = heapq.heappop(distance)
            res.append([x,y])
        
        return res