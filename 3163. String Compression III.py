class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        count = 0
        cur = word[0]
        for letter in word:
            if cur == letter:
                if count >= 9:
                    comp.append(str(count) + cur)
                    count = 1
                else:
                    count += 1
                    continue
            else:
                comp.append(str(count) + cur)
                count = 1
                cur = letter
        comp.append(str(count) + cur)
        
        return "".join(comp)