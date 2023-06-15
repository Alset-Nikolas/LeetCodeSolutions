from typing import * 

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = dict()
        d2 = dict()
        min_val = len(list1) + len(list2)
        for list_, d in zip([list1, list2], [d1,d2]):
            for i, x in enumerate(list_):
                if x in d:
                    continue
                d[x] = i
                if x in d1 and x in d2:
                    min_val = min(min_val, d1[x] + d2[x])
        res = []
        for k, v in d1.items():
            if k in d1 and k in d2:
                if d1[k] + d2[k] == min_val:
                    res.append(k)
        return res
        