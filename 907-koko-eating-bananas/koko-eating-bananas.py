class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search

        r = max(piles)
        lowest_k = r
        l = 1
        while l <= r:
            k = (r-l) // 2 + l
            hours_spent = 0
            for e in piles:
                hours_spent += math.ceil(e / k)
            if hours_spent > h:
                l = k+1
            else:
                r = k-1
                lowest_k = min(lowest_k, k)
        
        return lowest_k