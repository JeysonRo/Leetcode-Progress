class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        p1 = 0
        p2 = 0
        res = 1
        cur = 0
        bank = {}

        while p2 < len(s):
            if s[p2] not in bank:
                bank[s[p2]] = p2
                p2 += 1
                cur += 1
            else:
                del bank[s[p1]]
                p1 += 1
                cur -= 1
            res = max(res, cur)
        
        return res
