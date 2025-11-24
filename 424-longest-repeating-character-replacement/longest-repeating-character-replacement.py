class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def increment_char(char):
            if char not in chars:
                chars[char] = 0
                char_counts_index[0].add(char)
            char_counts_index[chars[char]].remove(char)
            chars[char] += 1
            if len(char_counts_index) <= chars[char]:
                char_counts_index.append(set())
            char_counts_index[chars[char]].add(char)

        def decrement_char(char):
            char_counts_index[chars[char]].remove(char)
            chars[char] -= 1
            char_counts_index[chars[char]].add(char)
        
        l = 0
        r = 0
        char_counts_index = [set()]
        chars = {}
        freq = 0
        while r < len(s):
            increment_char(s[r])

            if chars[s[r]] > freq:
                freq = chars[s[r]]

            while len(char_counts_index[freq]) == 0:
                freq -= 1
            if freq + k >= r-l + 1:
                r += 1
                continue
            
            r += 1
            decrement_char(s[l])
            l += 1
        
        return r-l
    