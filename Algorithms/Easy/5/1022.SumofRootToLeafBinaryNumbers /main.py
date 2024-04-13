# Definition for a binary tree node.
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def go_tree(node: Optional[TreeNode], pref: str ='') -> None:
            res = 0
            pref = pref + str(node.val)
            if not node.left and not node.right:
                print(pref, int(pref, 2))
                return int(pref, 2)
            if node.left:
                res += go_tree(node.left, pref)
            if node.right:
                res += go_tree(node.right, pref)
            return res
        res = go_tree(root, '')
        return res