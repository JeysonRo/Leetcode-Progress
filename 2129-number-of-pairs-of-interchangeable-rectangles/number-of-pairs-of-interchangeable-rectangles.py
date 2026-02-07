class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        
        ratios = [w/h for w, h in rectangles]
        ratio_count = {} # ratio : count

        res = 0
        for ratio in ratios:
            if ratio in ratio_count:
                res += ratio_count[ratio]
                ratio_count[ratio] += 1
            else:
                ratio_count[ratio] = 1
        
        return res