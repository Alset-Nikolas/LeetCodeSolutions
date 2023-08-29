from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Stack:
    def __init__(self):
        self.mass = []

    def add(self, x):
        if x:
            self.mass.append(x)

    def pop(self):
        return self.mass.pop()

    def is_empty(self):
        return self.mass == []


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        main_stack = Stack()
        main_stack.add(root)
        res = []
        while not main_stack.is_empty():
            buffer_stack = Stack()
            param = 0
            items = 0
            while not main_stack.is_empty():
                last_item = main_stack.pop()
                param += last_item.val
                items += 1
                buffer_stack.add(last_item.left)
                buffer_stack.add(last_item.right)
            main_stack = buffer_stack
            res.append(param / items)
        return res
