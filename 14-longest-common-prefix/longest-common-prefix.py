class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        shortest_word = len(strs[0])
        for word in strs:
            shortest_word = min(shortest_word, len(word))
        
        for i in range(shortest_word):
            prefix = word[i]
            for word in strs:
                if word[i] != prefix:
                    return lcp
            lcp += prefix
        return lcp