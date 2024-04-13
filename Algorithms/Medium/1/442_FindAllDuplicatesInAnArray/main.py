from typing import List


class Solution:
	def findDuplicates(self, nums: List[int]) -> List[int]:
		ans = set()
		for i in range(len(nums)):
			x = nums[i]
			j = abs(x) - 1
			if nums[j] > 0:
				nums[j] *= (-1)
			elif nums[j] < 0:
				ans.add(j + 1)
		return list(ans)