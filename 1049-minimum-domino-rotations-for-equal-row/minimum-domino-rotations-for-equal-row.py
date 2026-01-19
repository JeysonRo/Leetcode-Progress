class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        top = tops[0]
        bottom = bottoms[0]

        top_match_top = 0
        top_match_bottom = 0
        bottom_match_top = 0
        bottom_match_bottom = 0

        top_possible = True
        bottom_possible = True
        for i in range(n):
            if tops[i] != top and bottoms[i] != top:
                top_possible = False 
            if tops[i] != bottom and bottoms[i] != bottom:
                bottom_possible = False
            if not top_possible and not bottom_possible:
                return -1
            if top == tops[i]:
                top_match_top += 1
            if top == bottoms[i]:
                top_match_bottom += 1
            if bottom == tops[i]:
                bottom_match_top += 1
            if bottom == bottoms[i]:
                bottom_match_bottom += 1
        
        res = n
        if top_possible:
            res = min(n - top_match_top, n - top_match_bottom, res)
        if bottom_possible:
            res = min(n - bottom_match_top, n - bottom_match_bottom, res)
        return res