from typing import * 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Stack:
    def __init__(self):
        self.mass = []

    def is_empty(self):
        return self.mass == []
    
    def add(self, x:str):
        if self.is_empty():
            self.mass.append(x)
            return
        if x == ')' and self.show() == '(' :
            self.pop()
            return
        self.mass.append(x)
    
    def add_ignore(self, x):
        self.mass.append(x)
    
    def show(self):
        return self.mass[-1]
    
    def pop(self):
        return self.mass.pop()
    
    def ans(self):
        return ''.join(self.mass)

        
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node:Optional[TreeNode], stack:Stack):
            if not node:
                return
            stack.add(str(node.val))
            if node.left:
                stack.add('(')
                dfs(node.left, stack)
                stack.add(')')
            if node.right:
                stack.add('(')
                dfs(node.right, stack)
                stack.add(')')

        stack = Stack()
        dfs(root, stack)
        return stack.ans()

