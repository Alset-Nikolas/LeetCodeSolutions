class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        q = dict()
        items = set()
        for ti in t:
            if ti not in q:
                q[ti] = 0
                items.add(ti)
            q[ti] += 1
        for si in s:
            q[si] -= 1
            if q[si] == 0:
                items.remove(si)
        return items.pop()