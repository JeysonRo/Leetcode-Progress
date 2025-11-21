class WordDictionary:

    def __init__(self):
        self.children = defaultdict(WordDictionary)
        self.word = False

    def addWord(self, word: str) -> None:
        cur = self
        for i in word:
            if i not in cur.children:
                cur.children[i] = WordDictionary()
            cur = cur.children[i]
        cur.word = True

    def search(self, word: str) -> bool:
        cur = self

        for i in range(len(word)):
            c = word[i]

            if c == ".":
                for child in cur.children.values():
                    res = child.search(word[i+1:])
                    if res:
                        return True
                return False
            else:
                if c not in cur.children:
                    return False
                else:
                    cur = cur.children[c]
        return cur.word



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)