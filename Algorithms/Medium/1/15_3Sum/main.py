from typing import List


class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		res = set()
		nums.sort()
		for i in range(len(nums)):
			j = i + 1
			k = len(nums) - 1
			while j < k :
				sum_ = nums[i] + nums[j] + nums[k]
				if sum_ == 0:
					res.add(
						tuple(
							sorted([nums[i] , nums[j] , nums[k]])
						)
					)
					j += 1
					k-= 1
				elif sum_ < 0:
					j += 1
				else:
					k -= 1
		return list(list(x) for x in res)


# print(Solution().threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))