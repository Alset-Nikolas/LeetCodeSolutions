# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def create_bst(nums):
            len_ = len(nums)
            if not nums:
                return None

            center = TreeNode(val=nums[len_ // 2])
            center.left = create_bst(nums[:len_ // 2])
            center.right = create_bst(nums[len_ // 2 + 1:])
            return center

        return create_bst(nums)
