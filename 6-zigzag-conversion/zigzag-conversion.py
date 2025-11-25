class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows_str = ["" for i in range(numRows)]

        i = 0
        forward = True
        for c in s:
            if forward:
                rows_str[i] += c
                i += 1
            else:
                rows_str[i] += c
                i -= 1
            if i == 0:
                forward = True
            elif i == numRows-1:
                forward = False
        
        res = ""
        for str_list in rows_str:
            res += str_list
        return res