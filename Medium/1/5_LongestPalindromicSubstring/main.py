from collections import deque
class Solution:
	def convert(self, s: str, numRows: int) -> str:
		l = 0
		flag_up = True
		deques = [deque() for _ in range(numRows)]
		for i, si in enumerate(s):
			deques[l].append(si)
			if numRows > 1:
				if l == 0:
					flag_up = True
				if l == numRows - 1:
					flag_up = False
				l += bool(flag_up) if flag_up else -1

		res = []
		for deq in deques:
			while len(deq) > 0:
				res.append(deq.popleft())
		return ''.join(res)


print(Solution().convert(s='PAYPALISHIRING', numRows=3))
