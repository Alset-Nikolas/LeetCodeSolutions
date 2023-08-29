from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], mass):
            if not node:
                return 0
            pl = dfs(node.left, mass)
            pr = dfs(node.right, mass)
            val = node.val
            node.val = abs(pl - pr)
            mass.append(node.val)
            return val + pl + pr

        mass = []
        dfs(root, mass)
        return sum(mass)
