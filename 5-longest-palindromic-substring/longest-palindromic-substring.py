class Solution:
    def longestPalindrome(self, s: str) -> str:

        largest = 0
        largest_string = ''
        for i in range(len(s)):
            # odd
            l = i
            r = i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r-l+1 > largest:
                        largest = r-l + 1
                        largest_string = s[l:r+1]
                    l -= 1
                    r += 1
                else:
                    break
            # even
            l = i
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r-l+1 > largest:
                        largest = r-l + 1
                        largest_string = s[l:r+1]
                    l -= 1
                    r += 1
                else:
                    break
        
        return largest_string