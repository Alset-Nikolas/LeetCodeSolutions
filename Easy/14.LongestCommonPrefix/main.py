class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        min_len = len(min(strs, key=len))
        i = 0
        slovo = strs[0]
        while i < min_len:
            if all(x[i] == slovo[i]  for x in strs):
                i += 1
            else:
                break
        return slovo[:i]

if __name__ == "__main__":
    s = Solution()
    assert s.longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert s.longestCommonPrefix(["dog","racecar","car"]) == ''
    assert s.longestCommonPrefix([]) == ''
