from string import ascii_lowercase
from typing import *


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        info = {
            x: y for x, y in zip(ascii_lowercase, widths)
        }
        n = 1
        m = 0
        print(info)
        for x in [info[x] for x in s]:
            m += x
            if m > 100:
                n += 1
                m = x
                print(m)
        return [n, m]
