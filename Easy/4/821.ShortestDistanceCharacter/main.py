import math
from typing import *


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indexs_c = [math.inf]
        for i in range(len(s)):
            if s[i] == c:
                indexs_c.append(i)
        indexs_c.append(math.inf)
        res = []
        j = 0
        for i in range(len(s)):
            res.append(min(abs(i - indexs_c[j + 1]), abs(i - indexs_c[j])))
            if i == indexs_c[j + 1]:
                j += 1
        return res
