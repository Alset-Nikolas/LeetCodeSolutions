from typing import List


class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		info = {
			"2": "abc",
			"3": "def",
			"4": "ghi",
			"5": "jkl",
			"6": "mno",
			"7": "pqrs",
			"8": "tuv",
			"9": "wxyz"
		}
		if not digits:
			return []
		ans = ['']
		for si in digits:
			ansi = []
			for add_x in info[si]:
				for x in ans:
					ansi.append(x + add_x)
			ans = ansi
		return ans


# print(Solution().threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))