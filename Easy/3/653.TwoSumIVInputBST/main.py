from typing import * 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        items = set()
        def dfs(node, items):
            if not node:
                return
            items.add(node.val)
            dfs(node.left, items)
            dfs(node.right, items)
        dfs(root, items)

        for x in items:
            y = k - x
            if y in items:
                return True
        return False