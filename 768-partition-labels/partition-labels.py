class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        book = {}
        
        for i in range(len(s)):
            book[s[i]] = i
        
        i = 0
        r = 0
        res = []
        sumres = 0

        while i < len(s):
            r = max(book[s[i]], r)
            if i == r:
                res.append(i + 1 - sumres)
                sumres += res[-1]
            i += 1
        
        return res