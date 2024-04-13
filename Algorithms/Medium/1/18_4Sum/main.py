from typing import List


class Solution:
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
		res = set()
		nums.sort()

		for i in range(len(nums)-3):
			for j in range(i+1, len(nums)-2):
				k = j + 1
				l = len(nums) - 1
				while k < l and l > j:
					sum_ = nums[i] + nums[j] + nums[k] + nums[l]
					if sum_ == target:
						res.add(
							tuple(
								sorted([nums[i], nums[j], nums[k], nums[l]])
							)
						)
						k += 1
						l -= 1
					elif sum_ < target:
						k += 1
					else:
						l -= 1
		return list(list(x) for x in res)