class Solution:
	def __convert_res(self, mass):
		res = 0
		for i, x in enumerate(mass[::-1]):
			res += (10 ** i) * int(x)
		return res

	def myAtoi(self, s: str) -> int:
		if not s:
			return 0
		x_ = s
		while x_.startswith(' '):
			x_ = x_[1:]
		is_negative = False
		abs_x = x_
		if not abs_x:
			return 0
		if x_[0] == '-':
			is_negative = True
			abs_x = x_[1:]
		elif x_[0] == '+':
			abs_x = x_[1:]
		if not abs_x:
			return 0
		i = 0
		x = abs_x[i]

		res = []
		while x.isdigit() and i < len(abs_x):
			x = abs_x[i]
			if not x.isdigit():
				return self.__convert_res(res) * (-1) if is_negative else self.__convert_res(res)
			if is_negative:
				if -(1 << 31) > self.__convert_res(res + [int(x)]) * (-1):
					return -(1 << 31)
			else:
				if self.__convert_res(res + [int(x)]) > (1 << 31) - 1:
					return (1 << 31) - 1
			res.append(x)
			i += 1
		return self.__convert_res(res) * (-1) if is_negative else self.__convert_res(res)


print(Solution().myAtoi('-0012a42'))
