class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [0] * len(w)
        self.prefix[0] = w[0]
        for i in range(1, len(w)):
            self.prefix[i] = self.prefix[i-1] + w[i]

    def pickIndex(self) -> int:
        num = randint(1, self.prefix[-1])
        l = 0
        r = len(self.prefix) - 1
        while l < r:
            i = (l + r) // 2
            if num > self.prefix[i]:
                l = i + 1
            else:
                r = i
        return l
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()