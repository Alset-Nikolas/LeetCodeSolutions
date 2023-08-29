from collections import deque


class Solution(object):
    combination = {
        "(": ")",
        "[": "]",
        "{": "}",
    }

    def isValid(self, s):
        stack = deque()
        """
        :type s: str
        :rtype: bool
        """
        for symvol in s:
            if len(stack) == 0:
                if symvol not in self.combination.keys():
                    return False
                stack.append(symvol)
            else:
                if symvol in self.combination.keys():
                    stack.append(symvol)
                else:
                    if len(stack) == 0:
                        return False
                    last_symvol = stack.pop()
                    if self.combination[last_symvol] != symvol:
                        return False
        return len(stack) == 0


if __name__ == "__main__":
    s = Solution()
    assert s.isValid("()")
    assert s.isValid("()[]{}")
    assert not s.isValid("(]")
