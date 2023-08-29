from typing import *


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = None
        sumi = 0
        j = 0
        for i in range(len(nums)):
            sumi += nums[i]
            if j + k == i:
                res = sumi if not res else max(res, sumi)
                sumi -= nums[j]
                j += 1
        return res
