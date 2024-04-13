from typing import  List

class Solution:
	def sorted_slice(self, nums: List[int], l: int):
		for _ in range(l, len(nums)):
			for i in range(l, len(nums)-1):
				if nums[i] > nums[i + 1]:
					nums[i], nums[i + 1] = nums[i+1], nums[i]

	def get_p(self, nums, x, start):
		delta_ = None
		res = None
		for i in range(start, len(nums)):
			delta_i = nums[i] - x
			if delta_i <= 0:
				continue
			if delta_ is None or delta_i < delta_:
				res = i
				delta_ = delta_i
		return res

	def nextPermutation(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		if len(nums) <= 1:
			return
		l = len(nums) - 1
		while l - 1>=0 and nums[l] <= nums[l-1]:
			l -= 1
		if l == 0:
			return self.sorted_slice(nums, 0)
		p = self.get_p(nums, x=nums[l-1], start=l)
		nums[p], nums[l-1] = nums[l-1], nums[p]
		self.sorted_slice(nums, l)



print(Solution().nextPermutation([1,5,1]))
