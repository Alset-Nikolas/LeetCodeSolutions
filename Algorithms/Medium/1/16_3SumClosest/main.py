from typing import List


class Solution:
	def threeSumClosest(self, nums: List[int], target: int) -> int:
		min_res = None
		nums.sort()
		for i in range(len(nums)):
			j = i + 1
			k = len(nums) - 1
			while j < k :
				sum_ = nums[i] + nums[j] + nums[k]
				if sum_ == target:
					return target
				elif sum_ < target:
					j += 1
				else:
					k -= 1
				if min_res is None or abs(target - sum_) < abs(target-min_res):
					min_res = sum_
		return min_res


# print(Solution().threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))