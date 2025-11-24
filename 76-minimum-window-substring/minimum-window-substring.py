class Solution:
    def minWindow(self, s: str, t: str) -> str:
        require = {}
        char_bank = {}

        for c in t:
            if c not in require:
                require[c] = 0
                char_bank[c] = 0
            require[c] += 1
        
        
        l, r = 0, 0
        min_window = s
        valid = 0
        valid_string_found = False
        while r < len(s):
            if s[r] not in require:
                r += 1
                continue
            else:
                char_bank[s[r]] += 1
                if char_bank[s[r]] == require[s[r]]:
                    valid += 1
            while valid >= len(require):
                valid_string_found = True
                if len(min_window) > r+1-l:
                    min_window = s[l:r+1]
                if s[l] in char_bank:
                    char_bank[s[l]] -= 1
                    if char_bank[s[l]] < require[s[l]]:
                        valid -= 1
                l += 1
            r += 1

        return min_window if valid_string_found else ""