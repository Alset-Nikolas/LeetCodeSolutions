class Solution:
    convert = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9
    }

    def mey_int(self, num1: str):
        res = 0
        start = 0
        for x in num1[::-1]:
            res += 10 ** start * self.convert[x]
            start += 1
        return res

    def addStrings(self, num1: str, num2: str) -> str:
        num1 = self.mey_int(num1)
        num2 = self.mey_int(num2)
        res = num1 + num2
        if res == 0:
            return '0'
        ans = ''
        flag = False
        if res < 0:
            flag = True
        res = abs(res)
        while res > 0:
            ans = str(res % 10) + ans
            res //= 10
        if flag:
            ans = '-' + ans
        return ans
