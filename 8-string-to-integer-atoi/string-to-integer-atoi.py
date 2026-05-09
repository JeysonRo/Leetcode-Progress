import re
class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.search(r'(\A\s*)([-+]?)(0*)(\d*)', s)
        # group(0) whitespace
        # group(1) sign 
        # group(2) leading zeros
        # group(3) number
        
        left_limit = -2**31
        right_limit = 2**31 - 1
        negative = True
        if match.groups()[1] != '-':
            negative = False
        
        val = 0
        number = match.groups()[3]
        for i in range(len(number)):
            val *= 10
            if negative:
                val -= int(number[i])
            else:
                val += int(number[i])
            if not negative and val >= right_limit:
                return right_limit
            if negative and val <= left_limit:
                return left_limit
        
        return val