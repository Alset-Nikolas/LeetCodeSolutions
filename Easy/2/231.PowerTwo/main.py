class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <1:
            return False
        start = 1
        while n > start:
            start = start << 1
        return start == n