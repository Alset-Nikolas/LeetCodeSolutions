from typing import *

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return []
        l = nums[0]
        r = None
        res = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                r = nums[i]
            else:
                if r is None:
                    res.append(str(l))
                else:
                    res.append(f"{l}->{r}")
                l = nums[i]
                r = None
        if r:
            res.append(f"{l}->{r}")
        else:
            res.append(str(l))

        return res



