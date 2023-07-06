from typing import * 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_mass(root: Optional[TreeNode], mass):
            if not root:
                return 
            if not root.left  and not root.right:
                mass.append(root.val)
                return
            get_mass(root.left, mass)
            get_mass(root.right, mass)
        mass1 = []
        mass2 = []
        get_mass(root1, mass1)
        get_mass(root2, mass2)
        return mass1 == mass2

            
