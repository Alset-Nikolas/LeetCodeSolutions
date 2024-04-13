from typing import *


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return sorted(list(set(range(1, len(nums) + 1)) - set(nums)))
