class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp]) # store
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, []) # retrieve

        l = 0
        r = len(values) - 1
        res = ""

        while l <= r:
            m = l + (r - l) // 2
            m_value = values[m][0]
            m_timestamp = values[m][1] 

            if m_timestamp <= timestamp:
                res = m_value
                l = m + 1
            else:
                r = m - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)