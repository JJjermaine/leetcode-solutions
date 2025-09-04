class MyHashMap:

    def __init__(self):
        self.res = {}

    def put(self, key: int, value: int) -> None:
        #if key in self.res:
        self.res[key] = value
        #else:
        #    res[key] += value
        return self.res

    def get(self, key: int) -> int:
        if key in self.res:
            return self.res[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.res:
            del self.res[key]
        return self.res
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)