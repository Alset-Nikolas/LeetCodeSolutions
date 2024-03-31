from pprint import pprint


class Solution:
	def longestPalindrome(self, s: str) -> str:
		N = len(s) + 2
		F = [[0 for xi in range(N)] for j in range(N)]
		max_palin = ''

		for k in range(1, N - 1):
			j = 1
			for i in range(k, N - 1):
				if j == i:
					F[j][i] = 1
				else:
					if i - j > 1:
						F[j][i] = int(s[i - 1] == s[j - 1] and F[j + 1][i - 1])
					else:
						F[j][i] = int(s[i - 1] == s[j - 1])
				if F[j][i] and len(s[j-1: i]) >= len(max_palin) :
					max_palin = s[j-1: i]

				j = (j + 1) % (N - 1)

		return max_palin


print(Solution().longestPalindrome("aacabdkacaa"))
