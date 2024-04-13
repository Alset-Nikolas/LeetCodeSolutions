from typing import List


class Solution:
	def search(self, nums: List[int], target: int) -> int:
		l = 0
		r = len(nums) - 1
		while l <= r:
			m = (l + r) // 2
			if nums[m] == target:
				return m
			if nums[l] <= nums[m]:
				if nums[l] <= target <= nums[m]:
					r = m - 1
				else:
					l = m + 1
			else:
				if nums[l] <= target <= nums[m]:
					l = m + 1
				else:
					r = m - 1

		return -1


def run_tests():
	test1 = Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0)
	assert test1 == 4, test1

	test2 = Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3)
	assert test2 == -1, test2

	test3 = Solution().search(nums=[1], target=0)
	assert test3 == -1, test3

	test101 = Solution().search(nums=[1], target=1)
	assert test101 == 0, test101

	test111 = Solution().search(nums=[3, 1], target=3)
	assert test111 == 0, test111

	test145 = Solution().search(nums=[3,5,1], target=3)
	assert test145 == 0, test145

if __name__ == "__main__":
	items = list(map(int, input().split()))
	x = int(input())
	print(Solution().search(nums=items, target=x))
