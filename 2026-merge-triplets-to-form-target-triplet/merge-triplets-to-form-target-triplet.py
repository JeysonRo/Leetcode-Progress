class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        at, bt, ct = target
        afound = bfound = cfound = False
        for ai, bi, ci in triplets:
            if ai <= at and bi <= bt and ci <= ct: # suitable triplet
                if ai == at:
                    afound = True
                if bi == bt:
                    bfound = True
                if ci == ct:
                    cfound = True
            if afound and bfound and cfound:
                return True
        
        return False