from typing import *


# Definition for a Node.


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        res = 0
        info = dict()
        for x in nums:
            if x not in info:
                info[x] = 0
            info[x] += 1
        for k, v in info.items():
            if k + 1 in info:
                res = max(res, v * info[k + 1])
            elif k - 1 in info:
                res = max(res, v * info[k - 1])
        return res
