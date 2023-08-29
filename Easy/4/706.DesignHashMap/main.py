class Item:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val


class MyHashMap:

    def __init__(self):
        self.N = 999
        self.mass = [[] for x in range(self.N)]

    def put(self, key: int, value: int) -> None:
        hash_ = key % self.N
        item = Item(key, value)

        for x in self.mass[hash_]:
            if x.key == key:
                x.val = value
                return
        self.mass[hash_].append(item)

    def get(self, key: int) -> int:
        hash_ = key % self.N
        for x in self.mass[hash_]:
            if x.key == key:
                return x.val
        return -1

    def remove(self, key: int) -> None:
        hash_ = key % self.N
        for i, x in enumerate(self.mass[hash_]):
            if x.key == key:
                self.mass[hash_].pop(i)
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
