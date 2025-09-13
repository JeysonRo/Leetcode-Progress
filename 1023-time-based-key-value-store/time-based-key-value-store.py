class TimeMap:

    def __init__(self):
        self.table = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.table:
            self.table[key].append((value, timestamp))
        else:
            self.table[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.table:
            return ""
        l = 0
        r = len(self.table[key]) - 1
        lastvalid = ""
        while l <= r:
            i = (r - l) // 2 + l
            settime = self.table[key][i][1]
            if settime <= timestamp:
                lastvalid = self.table[key][i][0]
                l = i + 1
            else:
                r = i - 1

        return lastvalid


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)