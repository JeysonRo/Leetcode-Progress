class Solution:
    def minWindow(self, s: str, t: str) -> str:
        requiredmap = {}
        fulfilled = set()
        minlen = len(s) + 1
        answer = ""
        for c in t:
            requiredmap[c] = 1 + requiredmap.get(c, 0)

        contained = {}

        l = r = 0
        
        while r < len(s):
            if len(fulfilled) < len(requiredmap):
                if s[r] in requiredmap:
                    contained[s[r]] = contained.get(s[r], 0) + 1
                    if contained.get(s[r]) >= requiredmap.get(s[r]):
                        if s[r] not in fulfilled:
                            fulfilled.add(s[r])
                r += 1
            else: # fulfilled >= requiredmap
                if r-l < minlen:
                    minlen = r-l
                    answer = s[l:r]
                if s[l] in requiredmap:
                    contained[s[l]] = contained.get(s[l], 0) - 1
                    if contained.get(s[l]) < requiredmap.get(s[l]):
                        if s[l] in fulfilled:
                            fulfilled.remove(s[l])
                l += 1

        while l < len(s):
            if len(fulfilled) >= len(requiredmap):
                if r-l < minlen:
                    minlen = r-l
                    answer = s[l:r]
                if s[l] in requiredmap:
                    contained[s[l]] = contained.get(s[l], 0) - 1
                    if contained.get(s[l]) < requiredmap.get(s[l]):
                        if s[l] in fulfilled:
                            fulfilled.remove(s[l])
            l += 1

        return answer
