class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        adj = {}

        cache = {}

        for i, word in enumerate(wordDict):
            if word[0] in adj:
                adj[word[0]].append(i)
            else:
                adj[word[0]] = [i]
        
        def dfs(i): # i = s index
            if i >= len(s):
                return True
            if i in cache:
                return cache[i]
            if s[i] in adj:
                for j in adj[s[i]]: # j = index of words in worddict, matching start letter of s
                    word_len = len(wordDict[j])
                    if wordDict[j] == s[i:word_len+i]:
                        res = dfs(word_len+i)
                        if res:
                            cache[i] = True
                            return True
            cache[i] = False
            return False

        return dfs(0)