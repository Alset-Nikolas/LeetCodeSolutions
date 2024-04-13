class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        info = dict()
        for i in range(n):
            s_i, t_i = s[i], t[i]
            if s_i not in info:
                info[s_i] = t_i
            if info[s_i] != t_i:
                return False
        return len(set(s)) == len(set(t))


if __name__ == "__main__":
    s = Solution()
    assert s.isIsomorphic('egg', 'add')
    assert not s.isIsomorphic('foo', 'bar')
    assert s.isIsomorphic('paper', 'title')
