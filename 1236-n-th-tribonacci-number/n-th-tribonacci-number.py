class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0] * 38
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1

        for i in range(3, 38):
            memo[i] = memo[i-3] + memo[i-2] + memo[i-1]
        
        return memo[n]