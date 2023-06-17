from typing import * 

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_real = set(range(1, len(nums)+1))
        find_x = None
        for x in nums:
            if x in nums_real:
                nums_real.remove(x)
            else:
                find_x = x
        return [find_x, nums_real.pop()]