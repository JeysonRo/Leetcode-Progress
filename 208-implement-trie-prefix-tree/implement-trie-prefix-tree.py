class Trie:

    def __init__(self):
        self.pre = {} # list of starting chars pre[char] = list of next
        self.inserted = False

    def insert(self, word: str) -> None:
        trie = self
        for c in word:
            pre = trie.pre
            if c not in pre:
                pre[c] = Trie()
            trie = pre[c]
        trie.inserted = True
        
    def search(self, word: str) -> bool:
        trie = self
        for c in word:
            pre = trie.pre
            if c not in pre:
                return False
            trie = pre[c]
        if trie.inserted:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        pre = self.pre
        for c in prefix:
            if c in pre:
                pre = pre[c].pre
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)