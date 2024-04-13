class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0
        r = x
        while r > l:
            m = (l + r + 1) // 2
            if m * m > x:
                r = m - 1
            else:
                l = m
        return l


if __name__ == "__main__":
    s = Solution()
    assert s.mySqrt(4) == 2
    assert s.mySqrt(8) == 2
    assert s.mySqrt(0) == 0
