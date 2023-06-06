from string import ascii_uppercase

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """


        res = []
        n = columnNumber
        while n>0:
            n -= 1
            res.append(ascii_uppercase[n%26])
            n //= 26
        return ''.join(res[::-1])


if __name__ =="__main__":
    s = Solution()
    assert s.convertToTitle(28) =='AB'
    assert s.convertToTitle(701) =='ZY'
    assert s.convertToTitle(52) =='AZ'
