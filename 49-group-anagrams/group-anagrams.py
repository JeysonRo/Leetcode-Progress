class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        banks = []
        res = []

        for i in strs:
            worddict = {}
            for j in i:
                if j in worddict:
                    worddict[j] += 1
                else:
                    worddict[j] = 1
            if worddict not in banks:
                banks.append(worddict)
                res.append([])
            for k, bank in enumerate(banks):
                if bank == worddict:
                    print("I appended " + str(k))
                    res[k].append(i)

        return res