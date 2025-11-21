class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.scores = []
        self.k = k
        for i in nums:
            if len(self.scores) >= k:
                if i > self.scores[0]:
                    heapq.heapreplace(self.scores, i)
            else:
                heapq.heappush(self.scores, i)

    def add(self, val: int) -> int:
        if len(self.scores) < self.k:
            heapq.heappush(self.scores, val)
        elif val > self.scores[0]:
            heapq.heapreplace(self.scores, val)
        return self.scores[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)