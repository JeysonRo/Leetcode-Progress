class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (r - l) // 2 + l
            t = 0
            for i in piles:
                t += math.ceil(i/k)
            if t > h:
                l = k + 1
            elif t <= h:
                r = k - 1
                res = k
        return res

