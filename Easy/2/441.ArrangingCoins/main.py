class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1
        r = n
        a1 = 1
        while l < r:
            m = (l + r + 1) // 2
            am = a1 + 1 * (m - 1)
            sum_ = m * (a1 + am) // 2
            if sum_ == n:
                return m
            elif sum_ < n:
                l = m
            else:
                r = m - 1

        return l


print(Solution().arrangeCoins(8))
