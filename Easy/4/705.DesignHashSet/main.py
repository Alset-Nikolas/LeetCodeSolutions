from typing import *

class MyHashSet:

    def __init__(self):
        self.N = 999
        self.mass = [[] for x in range(self.N)]
        

    def add(self, key: int) -> None:
        index = key % self.N
        for x in self.mass[index]:
            if x == key:
                return
        self.mass[index].append(key)
        print(self.mass)


    def remove(self, key: int) -> None:
        index = key % self.N
        for i, x in enumerate(self.mass[index]):
            if x == key:
                self.mass[index].pop(i)
                return 
        

    def contains(self, key: int) -> bool:
        index = key % self.N
        for x in self.mass[index]:
            if x == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(3)
obj.remove(3)
