from sortedcontainers import SortedList

class MKAverage:

    def __init__(self, m: int, k: int):
        self.smallest = SortedList([])
        self.middle = SortedList([])
        self.largest = SortedList([])
        self.sum = 0
        self.m = m
        self.k = k
        self.stream = deque()

    def addElement(self, num: int) -> None:
        self.stream.append(num)
        if len(self.stream) > self.m:
            to_discard = self.stream.popleft()
            # find element to discard
            if to_discard > self.middle[-1]:
                self.largest.discard(to_discard)
            elif to_discard < self.middle[0]:
                self.smallest.discard(to_discard)
            else:
                self.sum -= to_discard
                self.middle.discard(to_discard)

        self.middle.add(num)
        self.sum += num
        while len(self.middle) > 0 and len(self.largest) < self.k:
            self.largest.add(self.middle[-1])
            self.sum -= self.middle[-1]
            self.middle.remove(self.middle[-1])
        while self.middle and self.middle[-1] > self.largest[0]:
            self.largest.add(self.middle[-1])
            self.sum -= self.middle[-1]
            self.middle.discard(self.middle[-1])
            self.sum += self.largest[0]
            self.middle.add(self.largest[0])
            self.largest.discard(self.largest[0])
        while len(self.middle) > 0 and len(self.smallest) < self.k:
            self.smallest.add(self.middle[0])
            self.sum -= self.middle[0]
            self.middle.remove(self.middle[0])
        while self.middle and self.middle[0] < self.smallest[-1]:
            self.sum += self.smallest[-1]
            self.middle.add(self.smallest[-1])
            self.smallest.discard(self.smallest[-1])
            self.smallest.add(self.middle[0])
            self.sum -= self.middle[0]
            self.middle.discard(self.middle[0])

    def calculateMKAverage(self) -> int:
        if len(self.smallest) + len(self.middle) + len(self.largest) < self.m:
            return -1
        return int(math.floor(self.sum / (self.m - 2 * self.k)))


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()