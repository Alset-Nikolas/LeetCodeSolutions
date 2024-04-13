class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n = len(a)
        m = len(b)
        res = ["0"] * (max(n, m) + 1)
        len_ = (max(n, m) + 1)
        flag = False
        for i in range(len(res)):
            x1 = 0 if i >= n else int(a[n - i - 1])
            x2 = 0 if i >= m else int(b[m - i - 1])
            sum_ = x1 + x2 + int(flag)
            if sum_ <= 1:
                res[len_ - i - 1] = str(sum_)
                flag = False
            elif sum_ == 2:
                flag = True
            else:
                res[len_ - i - 1] = "1"
                flag = True

        return "".join(res) if res[0] != "0" else "".join(res[1:])


if __name__ == "__main__":
    s = Solution()
    assert s.addBinary("11", "1") == "100"
    assert s.addBinary("1010", "1011") == "10101"
