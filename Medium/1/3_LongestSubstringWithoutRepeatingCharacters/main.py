from typing import List


class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		if len(s) <= 1:
			return len(s)
		l, r = 0, 0
		info = dict()
		res = -1

		for r in range(len(s)):
			x = s[r]
			if (x not in info) or (info[x] is None):
				info[x] = r
			else:
				res = max(res, r - l)
				new_l = info[x] + 1
				for li in range(l, new_l):
					info[s[li]] = None
				info[x] = r
				l = new_l
		else:
			res = max(res, len(s) - l)

		if l == 0:
			return len(s)

		return res

x = Solution().lengthOfLongestSubstring(s='abba')
print(x)