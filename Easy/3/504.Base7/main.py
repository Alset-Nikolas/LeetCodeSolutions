class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        res = ''
        flag = num < 0
        num = abs(num)
        while num != 0:
            res = str(num % 7) + res
            num = num // 7
        if flag:
            res = '-' + res

        return res
