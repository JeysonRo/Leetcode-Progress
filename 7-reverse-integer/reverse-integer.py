class Solution:
    def reverse(self, x: int) -> int:
        res = ''.join(reversed(str(x)))
        print(res)
        if res[-1] == "-":
            res = "-" + res[:-1]
        res = int(res)
        return res if res >= -2**31 and res < 2**31 else 0 