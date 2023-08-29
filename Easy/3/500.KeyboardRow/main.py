from typing import *


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        f1 = {x.lower() for x in 'qwertyuiop'}
        f2 = {x.lower() for x in 'asdfghjkl'}
        f3 = {x.lower() for x in 'zxcvbnm'}
        res = []
        for w in words:
            if any(x | {y.lower() for y in w} == x for x in [f1, f2, f3]):
                res.append(w)
        return res
