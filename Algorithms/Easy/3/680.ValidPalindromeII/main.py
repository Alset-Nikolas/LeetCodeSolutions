class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrom(s, i, j, flag=False):
            if i >= len(s) or j <= i or j < 0:
                return True
            if s[i] == s[j]:
                return check_palindrom(s, i + 1, j - 1, flag)
            if flag:
                return False
            l = check_palindrom(s, i + 1, j, True)
            r = check_palindrom(s, i, j - 1, True)
            return l or r

        return check_palindrom(s, 0, len(s) - 1)


print(Solution().validPalindrome("eeccccbebaeeabebccceea"))
