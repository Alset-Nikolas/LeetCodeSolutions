class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        l = 0
        r = num + 1
        while l < r:
            m = (l + r) // 2
            if m * m == num:
                return True
            elif m * m < num:
                l = m + 1
            else:
                r = m
        return False


print(Solution().isPerfectSquare(1))
