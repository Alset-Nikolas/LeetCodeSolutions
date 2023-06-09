class Solution:
    def longestPalindrome(self, s: str) -> int:
        items = dict()
        for si in s:
            if si not in items:
                items[si] = 0
            items[si] += 1
        res = 0
        flag = False
        for k, v in items.items():
            if v % 2 ==0:
                res += v
            else:
                flag = True
                res += v - 1
        return res + int(flag)