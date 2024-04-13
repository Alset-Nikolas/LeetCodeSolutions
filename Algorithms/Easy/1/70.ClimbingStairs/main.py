class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Fk = Fk_1 + Fk_2
        Fk = [0, 1, 2, 3]
        for i in range(n + 1):
            if i < len(Fk):
                continue
            Fk.append(Fk[i - 1] + Fk[i - 2])
        return Fk[n]


if __name__ == "__main__":
    s = Solution()
    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3
