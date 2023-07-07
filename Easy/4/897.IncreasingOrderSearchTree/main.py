from typing import * 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = [] 

        def bst(node, mass):
            if node.right:
                bst(node.right, mass)
            mass.append(node)
            if node.left:
                bst(node.left, mass)
        

        bst(root, stack)
        print([x.val for x in stack])
        head = stack.pop()
        head.left = None
        
        node = head
        while stack:
            node.right = stack.pop()
            node.right.left = None
            node = node.right
        return head