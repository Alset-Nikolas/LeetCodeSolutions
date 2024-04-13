from typing import List


class Solution:
	def bin_find_left(self, nums: List[int], target: int) -> int:
		l = 0
		r = len(nums) - 1
		ans = None
		while l <= r:
			m = (l + r) // 2
			if nums[m] < target:
				l = m + 1
			else:
				r = m - 1
				ans = m
		if l == len(nums):
			return - 1
		if ans is not None and nums[ans] == target:
			return ans
		return - 1

	def bin_find_right(self, nums: List[int], target: int) -> int:
		l = 0
		r = len(nums) - 1
		ans = None
		while l <= r:
			m = (l + r) // 2
			if nums[m] <= target:
				l = m + 1
				ans = m
			else:
				r = m - 1

		if r == -1:
			return - 1
		if ans is not None and nums[ans] == target:
			return ans
		return - 1

	def searchRange(self, nums: List[int], target: int) -> List[int]:
		l_ = self.bin_find_left(nums, target)
		r_ = self.bin_find_right(nums, target)
		return [l_, r_]


def run_tests():
	test1 = Solution().searchRange(
		nums=[5, 7, 7, 8, 8, 10],
		target=8
	)
	assert test1 == [3, 4], test1

	test2 = Solution().searchRange(
		nums=[5,7,7,8,8,10],
		target=6
	)
	assert test2 == [-1, -1], test2

	test3 = Solution().searchRange(
		nums=[],
		target=6
	)
	assert test3 == [-1, -1], test3

	test4 = Solution().searchRange(
		nums=[6],
		target=6
	)
	assert test4 == [0, 0], test4

if __name__ == "__main__":
	run_tests()
	items = list(map(int, input().split()))
	x = int(input())
	print(Solution().searchRange(nums=items, target=x))
