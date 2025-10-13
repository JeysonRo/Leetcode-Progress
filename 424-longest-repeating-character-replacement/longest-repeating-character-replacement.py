class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        longest = 0
        mfreq = 0
        freq = {0:set(), 1: set()}
        freq[0].add(s[l])
        bank = {s[l]: 0}

        def insertchar():
            if s[r] in bank:
                freq[bank[s[r]]].remove(s[r])
                bank[s[r]] += 1
                if bank[s[r]] in freq:
                    freq[bank[s[r]]].add(s[r])
                else:
                    freq[bank[s[r]]] = set([s[r]])
            else:
                bank[s[r]] = 1
                freq[bank[s[r]]].add(s[r])

        def removechar():
            freq[bank[s[l]]].remove(s[l])
            bank[s[l]] -= 1
            freq[bank[s[l]]].add(s[l])

        while r < len(s):
            insertchar() # highest freq char
            while mfreq + 1 in freq and len(freq[mfreq + 1]) > 0:
                mfreq += 1
            if len(freq[mfreq]) == 0:
                mfreq -= 1
            replacements = 1+r-l - mfreq # highest freq char
            if replacements <= k:
                longest = max(1+r-l, longest)
                r += 1
            else:
                removechar()
                l += 1
                r += 1

        return longest