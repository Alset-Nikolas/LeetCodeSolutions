from typing import * 

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        def calc_num_list(mass):
            res = 1
            for x in mass:
                res *= x
            return res
        return max(sum(nums[:3]), sum(nums[-3:]))