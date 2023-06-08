class Solution:
    def firstUniqChar(self, s: str) -> int:
        q = dict()
        j=0
        for i, x in enumerate(s):
            
            if x not in q:
                q[x] =0
            while j < len(s) and s[j] in q and s[j] <= 1:
                j += 1
            q[x] += 1
            