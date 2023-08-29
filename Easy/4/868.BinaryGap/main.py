class Solution:
    def binaryGap(self, n: int) -> int:
        mass = []
        while n > 0:
            mass.append(n % 2)
            n //= 2
        l = None
        ans = 0
        for r in range(len(mass)):
            if mass[r] == 1:
                if l is None:
                    l = r
                    continue
                ans = max(ans, r - l)
                l = r
        return ans
