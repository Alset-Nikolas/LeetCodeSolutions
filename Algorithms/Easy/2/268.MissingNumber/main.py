from typing import *


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all_numbers = set()
        max_ = 0
        for x in nums:
            if x > max_:
                max_ = x
            all_numbers.add(x)
        if max_ != len(nums):
            return max_ + 1
        x = set(range(max_)) - set(all_numbers)
        return x.pop()
