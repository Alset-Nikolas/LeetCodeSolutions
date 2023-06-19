from typing import * 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], val_root:int) -> int:
            if not node:
                return -1
            if not node.left:
                return -1
       
            if node.left.val == val_root:
                l = self.findSecondMinimumValue(node.left)   
            else:
                l = node.left.val           
            if node.right.val == val_root:
                r = self.findSecondMinimumValue(node.right)
            else:
                r = node.right.val

            return min(l, r) if l != -1 and r!=-1 else max(l, r)
        return dfs(root, root.val)
            
        
