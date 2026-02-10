class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # cardPoints = list of cards and their point values
        # each step, take 1 card from front or back
        # allowed "k" steps

        left_prefix = [0 for i in cardPoints]
        right_prefix = [0 for i in cardPoints]

        left_prefix[0] = cardPoints[0]
        for i in range(1, len(left_prefix)):
            left_prefix[i] = left_prefix[i-1] + cardPoints[i]

        right_prefix[len(right_prefix)-1] = cardPoints[len(right_prefix)-1]
        for i in range(len(right_prefix)-2, -1, -1):
            right_prefix[i] = right_prefix[i+1] + cardPoints[i]
        
        if k >= len(cardPoints):
            return right_prefix[0]
        
        l = k - 1
        r = len(cardPoints)
        res = left_prefix[l]
        while l >= -1:
            leftsum = 0 if l < 0 else left_prefix[l]
            rightsum = 0 if r >= len(right_prefix) else right_prefix[r]
            windowsum = leftsum + rightsum
            res = max(res, windowsum)
            l -= 1
            r -= 1
        
        return res