from typing import * 

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = 0
        sumi = 0
        j = 0 
        for i in range(len(nums)):
            sumi += nums[i]
            if j+k == i:
                res = max(res, sumi)
                j += 1
