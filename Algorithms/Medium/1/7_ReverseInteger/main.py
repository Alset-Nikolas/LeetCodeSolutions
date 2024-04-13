class Solution:
	def reverse(self, x: int) -> int:
		if x >0:
			x = int(str(x)[1::-1])
			TOP = (1 << 31) - 1
			if x > TOP:
				return 0
			return x
		DOWN = - (1 << 31)
		x = int(str(abs(x))[::-1])
		if x < DOWN:
			return 0
		return x
