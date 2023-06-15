from typing import * 
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        mass = []
        def dfs(node, mass:List):
            if not node:
                return
            [dfs(x, mass) for x in node.children]
            mass.append(node.val)
        dfs(root, mass)
        return mass