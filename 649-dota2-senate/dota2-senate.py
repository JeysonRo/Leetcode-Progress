class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        i = 0
        r_count = 0
        d_count = 0
        r_ban = 0
        d_ban = 0

        for c in senate:
            if c == 'R':
                r_count += 1
            if c == 'D':
                d_count += 1
        
        banned = set() # index of senators without rights

        while r_count > 0 and d_count > 0:
            if i >= len(senate):
                i = 0
            if i in banned:
                i += 1
                continue

            if senate[i] == "R":
                if r_ban > 0:
                    banned.add(i)
                    r_ban -= 1
                else:
                    d_ban += 1
                    d_count -= 1
            else:
                if d_ban > 0:
                    banned.add(i)
                    d_ban -= 1
                else:
                    r_ban += 1
                    r_count -= 1
            i += 1

        
        if d_count == 0:
            return "Radiant"
        else:
            return "Dire"