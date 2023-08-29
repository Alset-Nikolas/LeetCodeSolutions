from typing import *


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        info = dict()
        num_inds = dict()
        for i, x in enumerate(nums):
            if x not in info:
                info[x] = 0
                num_inds[x] = dict()
                num_inds[x]['start'] = i
            info[x] += 1
            num_inds[x]['end'] = i
        max_v = None
        res_k = []
        for k, v in info.items():
            if max_v is None:
                max_v = v
                res_k.append(k)
            else:
                if v > max_v:
                    max_v = v
                    res_k = []
                if v == max_v:
                    res_k.append(k)
        res = len(nums)
        for item in res_k:
            res = min(res, num_inds[item]['end'] - num_inds[item]['start'] + 1)

        return res
