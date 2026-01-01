class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 2 ** 31 - 1

        while (b & mask) > 0:
            tmp = (a & b) << 1
            a = a ^ b
            b = tmp
        
        return (a & mask) if b > 0 else a