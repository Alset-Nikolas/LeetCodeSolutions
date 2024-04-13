from typing import *


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        res = 0
        r_last = None
        for i in range(len(timeSeries)):
            li = timeSeries[i]
            if r_last is None:
                r_last = li + duration
                continue
            if li > r_last:
                res += duration
            else:
                delta = li - (r_last - duration)
                res += delta
            r_last = li + duration

        res += duration
        return res
