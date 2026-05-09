class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        def overlaps(a, b):
            if a[0] >= b[0] and a[0] <= b[1]:
                return True
            if a[1] >= b[0] and a[1] <= b[1]:
                return True
            if b[0] >= a[0] and b[0] <= a[1]:
                return True
            if b[1] >= a[0] and b[1] <= a[1]:
                return True
            return False

        def merge(a, b):
            start = min(a[0], b[0])
            end = max(a[1], b[1])
            return [start, end]
        
        intervals.sort(key=lambda x : x[0])
        merged_res = [intervals[0]]

        for i in range(1, len(intervals)):
            if overlaps(merged_res[-1], intervals[i]):
                merged_res[-1] = merge(merged_res[-1], intervals[i])
            else:
                merged_res.append(intervals[i])
        
        return merged_res