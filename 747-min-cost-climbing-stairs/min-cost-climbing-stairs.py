class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        back2 = cost[0]
        back1 = cost[1]
        
        i = 2
        while i < len(cost):
            steptotal = cost[i] + min(back1, back2)
            i += 1
            back2 = back1
            back1 = steptotal
            print(steptotal)

        return min(back1, back2)