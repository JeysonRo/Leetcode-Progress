class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if 0 == len(intervals):
            return [newInterval]

        res = []
        inserted = False
        
        for i in intervals:
            if not inserted and newInterval[1] < i[0]:
                res.append(newInterval.copy())
                inserted = True
                res.append(i)
            elif i[0] >= newInterval[0] and i[0] <= newInterval[1] or i[1] >= newInterval[0] and i[1] <= newInterval[1] or newInterval[0] >= i[0] and newInterval[1] <= i[1] or i[0] >= newInterval[0] and i[1] <= newInterval[1]:
                newInterval = [min(i[0], newInterval[0]), max(i[1], newInterval[1])]
                if res and res[-1][0] == newInterval[0]:
                    res[-1] = newInterval.copy()
                else:
                    res.append(newInterval.copy())
                inserted = True
            else:
                res.append(i)

        if inserted:
            return res
        else:
            res.append(newInterval.copy())
            return res