class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str: 
        if len(self.store[key]) == 0:
            return ""
        # binary search
        res = ""
        l = 0
        r = len(self.store[key]) - 1
        
        while l <= r:
            i = l + (r - l) // 2
            if self.store[key][i][0] > timestamp:
                r = i - 1
            else:
                res = self.store[key][i][1]
                l = i + 1
        
        return res
                

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)