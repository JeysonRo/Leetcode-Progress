class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        table = {}

        for c in s:
            table[c] = table.get(c, 0) + 1
        
        for c in t:
            if c in table and table[c] > 0:
                table[c] -= 1
            else:
                return False
        
        return True