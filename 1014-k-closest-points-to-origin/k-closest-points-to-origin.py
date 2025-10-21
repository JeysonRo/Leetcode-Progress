class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        table = {}
        heapq.heapify(distance)

        for i, vals in enumerate(points):
            x = vals[0]
            y = vals[1]
            val = (x**2 + y**2)
            if val in table:
                table[val].append(i)
            else:
                table[val] = [i]
            heapq.heappush(distance, val)
        
        res = []
        count = 0
        print(table)
        while count < k:
            count += 1
            val = heapq.heappop(distance)
            res.append(points[table[val].pop()])
        
        return res