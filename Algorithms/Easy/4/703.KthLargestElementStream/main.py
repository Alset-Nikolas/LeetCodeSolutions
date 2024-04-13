from typing import *


class MinHeap:
    def __init__(self, k) -> None:
        self.mass = []
        self.size = k

    def add_classic(self, x):
        self.mass.append(x)
        i = len(self.mass) - 1
        parent_i = (i - 1) // 2
        while i > 0 and self.mass[i] < self.mass[parent_i]:
            self.mass[i], self.mass[parent_i] = self.mass[parent_i], self.mass[i]
            i = parent_i
            parent_i = (i - 1) // 2

    def add(self, x):
        if len(self.mass) < self.size:
            self.add_classic(x)
        elif x >= self.get_min():
            self.pop_min()
            self.add_classic(x)
        print(self.mass)

    def pop_min(self):
        self.mass[0], self.mass[-1] = self.mass[-1], self.mass[0]
        self.mass.pop()
        i = 0
        l = 2 * i + 1
        r = 2 * i + 2
        while l < len(self.mass):
            j = l
            if r < len(self.mass) and self.mass[l] > self.mass[r]:
                j = r
            self.mass[i], self.mass[j] = self.mass[j], self.mass[i]
            i = j
            l = 2 * i + 1
            r = 2 * i + 2

    def get_min(self):
        return self.mass[0]


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = MinHeap(k)
        for x in nums:
            self.min_heap.add(x)

    def add(self, val: int) -> int:
        self.min_heap.add(val)
        return self.min_heap.get_min()

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
