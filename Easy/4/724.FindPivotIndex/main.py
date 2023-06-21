from typing import * 

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_r = sum(nums)
        sum_l = 0
        for i in range(len(nums)):
            x = nums[i]
            sum_l += x
            sum_r -= x
            if sum_l == sum_r:
                return i 
        return -1
