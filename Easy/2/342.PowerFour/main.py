from typing import *


class Solution:
    def countBits(self, n: int) -> List[int]:
        return [ sum(int(x) for x in bin(x)[2:]) for x in list(range(n+1))]
        
