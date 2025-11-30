class Solution:
    def findCoins(self, num_ways: List[int]) -> List[int]:
        n = len(num_ways)
        num_ways = [1] + num_ways
        my_ways = [1] + [0] * n
        res = []

        for i in range(1, n + 1):
            if my_ways[i] == num_ways[i]:
                continue
            
            if num_ways[i] - my_ways[i] == 1:
                res.append(i)
                for j in range(i, n + 1):
                    my_ways[j] += my_ways[j - i]
            
            else:
                return []
            
        return res