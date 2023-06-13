from typing import * 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node, mass=None):
            mass = mass or []
            if not node:
                return
            mass.append(node.val)
            dfs(node.left, mass)
            dfs(node.right, mass)
            return mass
        
        mass = dfs(root)
        mass.sort()
        res = abs(mass[0] - mass[1])
        for i in range(1, len(mass)):
            res = min(res, abs(mass[i] - mass[i-1]))
        return res
    
