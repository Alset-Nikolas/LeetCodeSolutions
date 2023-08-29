class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        str_x = str(x)
        n = len(str_x)
        for i in range(n // 2):
            if str_x[i] != str_x[n - i - 1]:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome(121)
    assert not s.isPalindrome(-121)
    assert not s.isPalindrome(10)
