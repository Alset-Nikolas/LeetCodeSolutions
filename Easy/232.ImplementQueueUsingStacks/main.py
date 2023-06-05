class MyQueue:

    def __init__(self):
        self.mass1 = []
        self.mass2 = []

    def push(self, x: int) -> None:
        self.mass1.append(x)


    def pop(self) -> int:
        if self.mass2 == []:
            while len(self.mass1) >0:
                self.mass2.append(self.mass1.pop())
        return self.mass2.pop()

        

    def peek(self) -> int:
        if self.mass2 == []:
            while len(self.mass1) >0:
                self.mass2.append(self.mass1.pop())
        return self.mass2[-1]
        

    def empty(self) -> bool:
        return self.mass1 == [] and self.mass2 == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()