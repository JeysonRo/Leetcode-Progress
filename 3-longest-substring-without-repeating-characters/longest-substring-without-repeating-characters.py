class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = set()

        l, r = 0, 0
        longest = 0
        while r < len(s):
            if s[r] in used:
                used.remove(s[l])
                l += 1
            else:
                used.add(s[r])
                r += 1
            longest = max(longest, r - l)
        return longest