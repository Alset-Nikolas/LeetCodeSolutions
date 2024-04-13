from typing import List

RIM_ = [
	(1, 'I'),
	(4, 'IV'),
	(5, 'V'),
	(9, 'IX'),
	(10, 'X'),
	(40, 'XL'),
	(50, 'L'),
	(90, 'XC'),
	(100, 'C'),
	(400, 'CD'),
	(500, 'D'),
	(900, 'CM'),
	(1000, 'M'),
]


class Solution:
	def intToRoman(self, num: int) -> str:
		res = []
		RIM_.sort(key=lambda x: x[0], reverse=True)
		for (val, rim) in RIM_:
			while num > 0 and  val <= num:
				res.append(rim)
				num -= val
			if num == 0:
				break
		return ''.join(res)


print(Solution().intToRoman(14))
