from typing import *


class NumArray:

    def __init__(self, nums: List[int]):
        self.sum_nums = [0] * (len(nums) + 1)
        self.nums = nums
        self.init_sum()

    def init_sum(self):
        for i, x in enumerate(self.nums):
            self.sum_nums[i + 1] = self.sum_nums[i] + x

    def sumRange(self, left: int, right: int) -> int:
        return self.sum_nums[right + 1] - self.sum_nums[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
