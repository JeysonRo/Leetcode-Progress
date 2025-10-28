class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()
        freq = {}

        for i in hand:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        i = 0
        total = 0
        while total < len(hand):
            if freq[hand[i]] == 0:
                i += 1
                continue
            for j in range(hand[i], hand[i] + groupSize):
                if j not in freq:
                    return False
                elif freq[j] <= 0:
                    return False
                freq[j] -= 1
                total += 1
            i += 1
        
        return True