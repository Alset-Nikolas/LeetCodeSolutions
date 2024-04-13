class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s) // 2):
            test = s[:i + 1]
            n = len(s) // len(test)
            if test * n == s:
                return True
        return False
