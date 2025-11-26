class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        for i, c in enumerate(s):
            if c == 'M':
                res += 1000
            elif c == 'D':
                res += 500
            elif c == 'C':
                if i+1 < len(s) and (s[i+1] == 'D' or s[i+1] == 'M'):
                    res -= 100
                else:
                    res += 100
            elif c == 'L':
                res += 50
            elif c == 'X':
                if i+1 < len(s) and (s[i+1] == 'L' or s[i+1] == 'C'):
                    res -= 10
                else:
                    res += 10
            elif c == 'V':
                res += 5
            elif c == 'I':
                if i+1 < len(s) and (s[i+1] == 'V' or s[i+1] == 'X'):
                    res -= 1
                else:
                    res += 1
        
        return res