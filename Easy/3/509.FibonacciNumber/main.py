class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        res = 0
        for x in range(1, int(num**0.5)+1):
            if x == num:
                continue
            if num % x == 0:
                res += x
                print(x, num // x)
                if x != 1 and num // x > num**0.5:
                    res += num // x
        return res == num