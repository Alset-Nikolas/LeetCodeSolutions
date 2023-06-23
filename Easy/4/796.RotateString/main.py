from typing import * 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        mass = []
        def dfs(node, mass):
            if not node:
                return 
            dfs(node.left, mass)
            mass.append(node.val)
            dfs(node.right, mass)
            
        dfs(root, mass)
        min_delta = 10**10
        for i in range(1,len(mass)):
            min_delta = min(min_delta, abs(mass[i]-mass[i-1] ))
        return min_delta