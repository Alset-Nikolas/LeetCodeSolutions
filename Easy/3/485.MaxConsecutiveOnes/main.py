class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = ''
        l = 0
        for t in s[::-1]:
            if t == '-':
                continue
            if l == k:
                res = '-' + res
                l = 0
            res = t.upper() + res
            l += 1
        return res


print(Solution().licenseKeyFormatting("5F3Z-2e-9-w", 4))
