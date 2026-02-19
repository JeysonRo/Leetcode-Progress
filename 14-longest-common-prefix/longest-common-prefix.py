class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        MAX_LEN = float("inf")
        for i in range(len(strs)):
            length = len(strs[i])
            MAX_LEN = min(MAX_LEN, length)
        
        res = ""
        for i in range(MAX_LEN):
            cur_letter = strs[0][i]
            for j in range(len(strs)):
                if cur_letter != strs[j][i]:
                    return res
            res += cur_letter

        return res