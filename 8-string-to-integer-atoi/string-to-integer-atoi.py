class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        digits = set(['0','1','2','3','4','5','6','7','8','9'])
        res = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i < len(s) and s[i] == "-":
            negative = True
            i += 1
        elif i < len(s) and s[i] == "+":
            negative = False
            i += 1
        else:
            negative = False
        
        while i < len(s) and s[i] == "0":
            i += 1

        while i < len(s) and s[i] in digits:
            res = res*10 + int(s[i])
            i += 1
            if negative:
                if res >= 2**31:
                    return -2**31
            elif res >= 2**31-1:
                return 2**31-1
        
        if negative:
            return -res
        else:
            return res