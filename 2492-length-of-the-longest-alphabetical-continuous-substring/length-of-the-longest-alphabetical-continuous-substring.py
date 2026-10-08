class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        res = 0
        cur = 1

        for i in range(1, len(s)):
            if ord(s[i]) == ord(s[i-1]) + 1:
                cur += 1
                res = max(res, cur)
            else:
                cur = 1
        res = max(res, cur)
        return res                