from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def go_down(node: Optional[TreeNode], pref=None):
            pref = pref or []
            if not node:
                return
            pref.append(str(node.val))
            if not node.left and not node.right:
                ans.append('->'.join(pref))
                return

            go_down(node.left, pref.copy())
            go_down(node.right, pref.copy())

        go_down(root)
        return ans
