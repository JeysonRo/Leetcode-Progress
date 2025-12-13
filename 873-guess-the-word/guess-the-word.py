# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        swap = True
        while len(words) > 0:
            if swap:
                matches = master.guess(words[0])
                match_word = words[0]
            else:
                matches = master.guess(words[len(words)-1])
                match_word = words[len(words)-1]
            new_list = []
            for i in range(len(words)):
                word = words[i]
                if word == match_word:
                    continue
                matching = 0
                for j in range(6):
                    if word[j] == match_word[j]:
                        matching += 1
                if matching == matches:
                    new_list.append(word)
            words = new_list
            swap = not swap