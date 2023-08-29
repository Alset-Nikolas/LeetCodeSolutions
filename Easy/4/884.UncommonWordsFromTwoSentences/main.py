from typing import *


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_info = dict()
        for w in s1.split():
            if w not in s1_info:
                s1_info[w] = 0
            s1_info[w] += 1
        s2_info = dict()
        for w in s2.split():
            if w not in s2_info:
                s2_info[w] = 0
            s2_info[w] += 1
        res = []
        for w in s1_info.keys() ^ s2_info.keys():
            if w in s1_info and s1_info[w] == 1 or w in s2_info and s2_info[w] == 1:
                res.append(w)
        return res
