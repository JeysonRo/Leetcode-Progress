class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        q = []
        events.sort()
        res = 0
        cur_day = events[0][0]
        for start,end in events:
            while q and cur_day < start:
                event_end = heapq.heappop(q)
                if event_end >= cur_day:
                    res += 1
                    cur_day += 1
            heapq.heappush(q, end)
            cur_day = start

        while q:
            event_end = heapq.heappop(q)
            if event_end >= cur_day:
                cur_day += 1
                res += 1
        
        return res

        # Time O(nlogn + nlogn + nlogn)
        # Space O(n)