class Solution:
    def hammingWeight(self, n: int) -> int:
        x = 0
        n_ = n
        for _ in range(32):
            x += n_ % 2
            n_ = n_ >> 1
        return x