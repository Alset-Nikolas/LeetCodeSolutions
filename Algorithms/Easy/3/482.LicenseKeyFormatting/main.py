from typing import *


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(0)
        l = 0
        li = 0
        for x in nums:
            if x == 1:
                li += 1
            else:
                l = max(li, l)
                li = 0
        return l
