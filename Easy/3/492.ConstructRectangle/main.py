from typing import *


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        ans = []
        for wi in range(1, area + 1):
            li = area // wi
            if wi * li == area and li >= wi:
                if ans == []:
                    ans = [li, wi]
                    continue
                if abs(ans[0] - ans[1]) > abs(wi - li):
                    ans = [li, wi]
        return ans
