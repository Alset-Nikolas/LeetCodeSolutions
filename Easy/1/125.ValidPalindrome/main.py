class Solution(object):
    def isPalindrome(self, s:str):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s_arr = []
        for s_i in s:
            if ord("a") <= ord(s_i) <= ord('z') or ord("0") <= ord(s_i) <= ord('9'):
                s_arr.append(s_i)
        s = ''.join(s_arr)
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama")