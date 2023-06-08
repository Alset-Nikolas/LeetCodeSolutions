class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        q = dict()
        for t in magazine:
            if t not in q:
                q[t] = 0
            q[t] += 1
        for t in ransomNote:
            if t not in q:
                return False
            q[t] -= 1
            if q[t] < 0:
                return False
        return True