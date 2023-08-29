from typing import *


class Stack:
    def __init__(self) -> None:
        self.mass = []

    def add(self, x):
        try:
            self.mass.append(int(x))
        except:
            self.mass.append(x)

    def pop(self):
        return self.mass.pop()

    def is_empty(self):
        return self.mass == []

    def check(self):
        return self.mass[-1]

    def sum(self):
        self.mass.append(self.mass[-1] + self.mass[-2])

    def x2(self):
        self.mass.append(self.mass[-1] * 2)


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = Stack()
        for x in operations:
            if x not in ["C", "D", "+"]:
                s.add(x)
            elif x == 'C':
                s.pop()
            elif x == 'D':
                s.x2()
            elif x == '+':
                s.sum()
        return sum(s.mass) if s.mass else 0
