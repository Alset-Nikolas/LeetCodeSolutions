from typing import List


class Solution:
	def calc_ans(self, height: List[int], l: int, r: int):
		return min(height[l], height[r]) * (r - l)

	def maxArea(self, height: List[int]) -> int:
		l = 0
		r = len(height) - 1
		ans_ = -1
		while l < r:
			ans_ = max(self.calc_ans(height, l, r), ans_)
			if height[l] <= height[r]:
				l += 1
			else:
				r -= 1
		return ans_

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
