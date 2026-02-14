class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        cur_bank = defaultdict(int) # letter : count
        sticker_bank = [{} for i in range(len(stickers))] # letter : count (for each sticker)
        letter_find = defaultdict(set) # letter : set of stickers containing this letter

        for i, word in enumerate(stickers):
            for c in word:
                if c in sticker_bank[i]:
                    sticker_bank[i][c] += 1
                else:
                    sticker_bank[i][c] = 1
                if i not in letter_find[c]:
                    letter_find[c].add(i)

        # for each char in target, choose a sticker that contains that letter, and add that sticker's letters to cur_bank
        
        @cache
        def dfs(word):
            if len(word) == 0:
                return 0
            res = len(target) + 1
            for sticker in letter_find[word[0]]:
                cur_bank = defaultdict(int)
                for key in sticker_bank[sticker]:
                    cur_bank[key] += sticker_bank[sticker][key]
                result_word = ''
                for c in word:
                    if c in cur_bank and cur_bank[c] > 0:
                        cur_bank[c] -= 1
                    else:
                        result_word = result_word + c
                res = min(res, dfs(result_word) + 1)
            return res

        res = dfs(target)
        return -1 if res > len(target) else res