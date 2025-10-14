class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        bank = {}
        chartotal = len(s1)
        for c in s1:
            if c in bank:
                bank[c] += 1
            else:
                bank[c] = 1
        
        l = r = 0
        charcount = 0
        while r < len(s2):
            if s2[r] in bank:
                if bank[s2[r]] <= 0:
                    bank[s2[l]] += 1
                    l += 1
                    charcount -= 1
                else:
                    bank[s2[r]] -= 1
                    r += 1
                    charcount += 1
            else:
                while l < r:
                    bank[s2[l]] += 1
                    l += 1
                    charcount -= 1
                r += 1
                l = r
            if charcount == chartotal:
                return True

        return False