class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        lower_bound = 0
        upper_bound = 2**(n-1)
        cur = 0

        for it in range(n-1):
            mid = lower_bound + (upper_bound - lower_bound) // 2
            if mid >= k:
                upper_bound = mid
            else:
                lower_bound = mid + 1
                cur = 1 if cur == 0 else 0
        
        return cur