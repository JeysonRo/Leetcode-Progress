class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # cardPoints = list of cards and their point values
        # each step, take 1 card from front or back
        # allowed "k" steps
        
        prefix = 0
        for i in range(k):
            prefix += cardPoints[i]
        
        l = k
        r = len(cardPoints) - 1
        res = prefix

        while l >= 0:
            res = max(res, prefix)
            l -= 1
            prefix -= cardPoints[l]
            prefix += cardPoints[r]
            r -= 1
        
        return res