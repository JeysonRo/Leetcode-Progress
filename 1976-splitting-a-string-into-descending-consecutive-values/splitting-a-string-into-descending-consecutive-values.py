class Solution:
    def splitString(self, s: str) -> bool:
        # decision tree
        # decide between including current digit in current group, or end current number and include it in next group

        def get_next(i, num = None): # starting from index i, iterate through string to find if equal to num
            cur_num = 0
            while i < len(s) and s[i] == '0':
                i += 1
            if i == len(s):
                if num == 0:
                    return True
                else:
                    return False
            while i < len(s) and cur_num < num:
                cur_num *= 10
                cur_num += int(s[i])
                i += 1
            if cur_num == num:
                if i == len(s):
                    return True
                else:
                    return get_next(i, num - 1)
            return False
        
        for i in range(1, len(s)):
            if get_next(i, int(s[0:i]) - 1):
                return True
        
        return False