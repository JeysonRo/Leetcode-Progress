class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        base = 29
        mod = 10**9 + 7
        power = base ** (len(needle) - 1)
        encoded_needle = 0
        encoded_word = 0

        for i in range(len(needle)):
            char = (ord(needle[i]) - ord('a') + 1)

            encoded_needle = (encoded_needle * base) % mod
            encoded_needle = (encoded_needle + char) % mod

            char = (ord(haystack[i]) - ord('a') + 1)

            encoded_word = (encoded_word * base) % mod
            encoded_word = (encoded_word + char) % mod

        if encoded_needle == encoded_word:
            return 0

        for i in range(len(needle), len(haystack)):
            # remove first character in hash
            char = (ord(haystack[i-len(needle)]) - ord('a') + 1)
            
            encoded_word = (encoded_word - (char * power)) % mod

            # insert next character
            char = (ord(haystack[i]) - ord('a') + 1)

            encoded_word = (encoded_word * base) % mod
            encoded_word = (encoded_word + char) % mod

            if encoded_needle == encoded_word:
                return i - len(needle) + 1
        
        return -1