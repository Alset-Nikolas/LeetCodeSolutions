from typing import List


class Solution:
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
		nums.sort()
# print(Solution().threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))