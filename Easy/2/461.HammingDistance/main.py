class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum(int(x == '1') for x in bin(x ^ y)[2:])
