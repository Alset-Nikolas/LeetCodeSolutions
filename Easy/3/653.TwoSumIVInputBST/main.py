from typing import * 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        items = dict()
        def dfs(node, items):
            if not node:
                return
            if node.val not in items:
                items[node.val] = 0
            items[node.val] += 1
            dfs(node.left, items)
            dfs(node.right, items)
        dfs(root, items)

        for x, q in items.items():
            y = k - x
            if x == y and q > 1:
                return True
            if x != y and y in items:
                return True
        return False