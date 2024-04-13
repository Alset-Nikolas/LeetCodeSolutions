from string import ascii_uppercase


class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        res = 0
        for i, x in enumerate(columnTitle[::-1]):
            res += 26 ** i * (ascii_uppercase.find(x) + 1)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.titleToNumber('ZY'))
