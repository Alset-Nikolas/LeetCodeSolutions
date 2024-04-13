from typing import *


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> List[int]:
        mass = []

        def dfs(node, mass: List[int]):
            if not node:
                return
            mass.append(node.val)
            [dfs(x, mass) for x in node.children]

        dfs(root, mass)
        return mass
