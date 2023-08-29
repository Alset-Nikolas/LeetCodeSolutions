class Solution(object):
    numbers = {
        None: 0,
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,

    }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i = 0
        while i < len(s):
            t = s[i]
            t_next = s[i + 1] if i + 1 < len(s) else None
            x_ = self.numbers[t]
            if t_next is None:
                res += x_
                i += 1
                continue
            x_next = self.numbers[t_next]
            if x_ < x_next:
                res += x_next - x_
                i += 2
                continue
            res += x_
            i += 1

        return res


if __name__ == "__main__":
    s = Solution()
    assert s.romanToInt("III") == 3
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994
