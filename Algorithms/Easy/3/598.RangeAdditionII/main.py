from typing import *


# Definition for a Node.
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if ops == []:
            return m * n
        return min(x for x, y in ops) * min(y for x, y in ops)
