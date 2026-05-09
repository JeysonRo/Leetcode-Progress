class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        letter_bank = {}
        fulfilled = set()
        gap = len(p)
        res = []
        for c in p:
            letter_bank[c] = letter_bank.get(c, 0) + 1
        
        current_bank = {}

        for i in range(len(s)):
            if s[i] in letter_bank:
                current_bank[s[i]] = current_bank.get(s[i], 0) + 1
                if current_bank[s[i]] >= letter_bank[s[i]] and s[i] not in fulfilled:
                    fulfilled.add(s[i])
            if i >= gap:
                if s[i-gap] in current_bank:
                    current_bank[s[i-gap]] -= 1
                    if current_bank[s[i-gap]] < letter_bank[s[i-gap]] and s[i-gap] in fulfilled:
                        fulfilled.remove(s[i-gap])
            if len(fulfilled) >= len(letter_bank):
                res.append(i - gap+1)
        
        return res