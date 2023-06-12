from typing import * 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root: Optional[TreeNode], info=None):
            info = info or {}
            if not root:
                return info
            if root.val not in info:
                info[root.val] = 0
            info[root.val] += 1
            info = dfs(root.left, info)
            info = dfs(root.right, info)
            return info
        info = dfs(root)
        res = []
        max_q = 0
        for k, v in info.items():
            if max_q == v:
                res.append(k)
            elif v > max_q:
                res = [k]
                max_q = v
        return res

