class Solution:
    def isUgly(self, n: int) -> bool:
        for x in [2, 3, 5]:
            while n >= x and n % x == 0:
                n //= x
        return n == 1
                
        

if __name__ == "__main__":
    s = Solution()
    assert s.isUgly(6)
    assert s.isUgly(1)
    assert not s.isUgly(14)


    