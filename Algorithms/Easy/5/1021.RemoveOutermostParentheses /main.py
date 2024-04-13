class Steck:
    def __init__(self):
        self.mass = []

    def add(self, x):
        if self.is_empty():
            self.mass.append(x)
            return
        last_simvol = self.pop()
        if last_simvol == '(' and x == ')':
            return
        self.mass.append(last_simvol)
        self.mass.append(x)

    def pop(self):
        return self.mass.pop()

    def is_empty(self):
        return self.mass == []


class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = Steck()
        i = 0
        ans = []
        for j, si in enumerate(s):
            stack.add(si)
            if stack.is_empty():
                ans.append(s[i + 1:j])
                i = j+1
        return ''.join(ans)


if __name__ == '__main__':
    text = "(()())(())"
    s = Solution()
    s.removeOuterParentheses(text)
