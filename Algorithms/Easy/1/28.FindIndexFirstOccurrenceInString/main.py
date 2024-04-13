class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # try:
        #     return haystack.index(needle)
        # except ValueError:
        #     return -1

        for i in range(len(haystack) - len(needle)):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.strStr('sadbutsad', 'sad') == 0
    assert s.strStr('leetcode', 'leeto') == -1
    assert s.strStr('mississippi', 'issip') == 4
