from typing import *

class MyStack:

    def __init__(self):
        self.mass = []

    def push(self, x: int) -> None:
        self.mass.append(x)

    def pop(self) -> int:
        return self.mass.pop()

    def top(self) -> int:
        return self.mass[-1]

    def empty(self) -> bool:
        return self.mass == []

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


