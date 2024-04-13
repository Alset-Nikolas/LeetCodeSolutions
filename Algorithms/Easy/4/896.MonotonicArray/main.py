from typing import *


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        flag = nums[0] >= nums[-1]
        for i in range(1, len(nums)):
            if not (nums[i] <= nums[i - 1] if flag else nums[i] >= nums[i - 1]):
                return False
        return True
