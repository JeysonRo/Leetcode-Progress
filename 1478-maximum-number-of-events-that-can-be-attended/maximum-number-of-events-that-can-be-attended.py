class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # O(n) where n is the amount of days from the start of the first event to the end of the last event
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