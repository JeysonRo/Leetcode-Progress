class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[0])
        removed = 0
        cur_start = intervals[0][0]
        cur_end = intervals[0][1]
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if cur_end > start: # overlapping
                removed += 1
                if cur_end > end:
                    cur_start = start
                    cur_end = end
            else:
                cur_start = start
                cur_end = end
            
        return removed