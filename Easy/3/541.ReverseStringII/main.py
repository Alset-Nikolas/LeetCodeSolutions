# Definition for a binary tree node.
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list = [x for x in s]
        for ik in range(len(s_list) // k + 1):
            if ik % 2 == 0:
                if k * (ik + 2) < len(s_list) or (k * (ik + 1) < len(s_list) and k * (ik + 2) >= len(s_list)):
                    s_list[k * ik:k * (ik + 1)] = s_list[k * ik:k * (ik + 1)][::-1]
                elif k * (ik + 1) >= len(s_list):
                    s_list[k * ik:] = s_list[k * ik:][::-1]

        return ''.join(s_list)


print(Solution().reverseStr('abcdefg', 8))
