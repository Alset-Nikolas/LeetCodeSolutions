# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = 2 ** 31 - 1
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m - 1
            else:
                l = m
        return l
