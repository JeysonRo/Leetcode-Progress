class Solution:
    def reverse(self, x: int) -> int:
        MIN = 2147483648
        MAX = 2147483647

        positive = x >= 0
        x = abs(x)
        res = 0

        while x > 0:
            digit = x % 10
            x = x // 10

            if positive and (res >  MAX // 10 or res == MAX // 10 and digit > MAX % 10):
                return 0
            if not positive and (res > MIN // 10 or res == MIN // 10 and digit > MIN % 10):
                return 0

            res = res * 10 + digit

        return res if positive else -res