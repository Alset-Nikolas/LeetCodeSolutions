from typing import * 

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)//2):
            res += min(nums[2*i],nums[2*i +1 ])
        return res