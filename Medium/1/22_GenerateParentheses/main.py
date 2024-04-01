from typing import List, Optional


class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		def recursion_go(n_open, m_close, ans, pref=None):
			pref = pref or []
			if n_open == 0 and m_close == 0:
				ans.append(''.join(pref))
				return
			if n_open > 0:
				recursion_go(n_open - 1, m_close,ans=ans, pref=pref + ['('])
			if n_open < m_close:
				recursion_go(n_open, m_close - 1,ans=ans, pref=pref +[')'])
			return ans
		ans = []
		recursion_go(n_open=n, m_close=n, ans=ans)
		return ans
print(Solution().generateParenthesis(3))