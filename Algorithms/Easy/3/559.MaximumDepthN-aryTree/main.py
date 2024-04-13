# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Node) -> int:
        if not root:
            return 0
        h = [self.maxDepth(x) for x in root.children] + [0]
        return max(h) + 1
