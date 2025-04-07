class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        invertedStones = [i * -1 for i in stones]
        heapq.heapify(invertedStones)

        while len(invertedStones) > 1:
            y = heapq.heappop(invertedStones)
            x = heapq.heappop(invertedStones)

            smash = y - x
            if smash < 0:
                heapq.heappush(invertedStones, smash)

        if len(invertedStones) == 1:
            return heapq.heappop(invertedStones) * -1
        else:
            return 0
