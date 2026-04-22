class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # get minimum eating speed that finishes under h time
        # range between 1 and max(piles)
        # binary search
        # find k such that cur_time > h and k+1 where cur_time <= h
        r = max(piles)
        l = 1
        while l < r:
            k = l + (r - l) // 2 
            cur_h = 0
            for pile in piles:
                if k >= pile:
                    cur_h += 1
                else:
                    cur_h += math.ceil(pile / k)
                    
            if cur_h > h: # K IS TOO SLOW
                l = k + 1
            else: # K is in time
                r = k
        
        return r
        # [3,6,7,11] 8
        # l = 1
        # r = 11
        # k = 5
        # cur = 5