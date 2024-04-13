from typing import *


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for x in range(left, right + 1):
            if 0 in set(int(sx) for sx in str(x)):
                continue
            if all(x % xi == 0 for xi in list(int(sx) for sx in str(x))):
                res.append(x)
        return res
