class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        res = [0 for i in range(N)]

        def recurs(i):
            if res[i] != 0:
                return res[i]
            if i > 0 and i < N - 1:
                if ratings[i] > ratings[i+1] and ratings[i] > ratings[i-1]:
                    res[i] = max(recurs(i-1), recurs(i+1)) + 1
                    return res[i]
            if i < N - 1:
                if ratings[i] > ratings[i+1]:
                    res[i] = recurs(i+1) + 1
                    return res[i]
            if i > 0:
                if ratings[i] > ratings[i-1]:
                    res[i] = recurs(i-1) + 1
                    return res[i]
            res[i] = 1
            return res[i]

        final = 0
        for i in range(N):
            final += recurs(i)
        
        return final