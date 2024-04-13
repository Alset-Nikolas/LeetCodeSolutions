class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = None
        while n > 0:
            if x is None:
                x = n % 2
            else:
                if x == n % 2:
                    return False
                x = n % 2
            n //= 2
        return True
