class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        res = [1 for i in range(N)]

        for i in range(1, N):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1
        
        for i in range(N-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                res[i] = max(res[i], res[i+1] + 1)
        
        final = 0
        for num in res:
            final += num
        return final