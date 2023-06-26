from typing import * 
from string import ascii_lowercase

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        info = {
            x: y for x, y in zip(ascii_lowercase, widths)
        }
        n=1
        m = 0
        for x in [info[x] for x in s]:
            m += x
            if m > 100:
                n += 1
                m -=100 
        return [n, m]