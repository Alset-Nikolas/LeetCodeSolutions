from typing import *


class Solution:
    def calc_ans(self, board: List[List[str]], i, j) -> int:
        res = 0
        for sigma in [1, -1]:
            flag = True
            for k in range(i, max(-1, sigma * 8), sigma):
                if board[k][j].upper() == 'B':
                    flag = False
                    break
                elif board[k][j].upper() == 'P' and flag:
                    res += 1
                    break
            flag = True
            for k in range(j, max(-1, sigma * 8), sigma):
                if board[i][k].upper() == 'B':
                    flag = False
                    break

                elif board[i][k].upper() == 'P' and flag:
                    res += 1
                    break
        return res

    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    return self.calc_ans(board, i, j)
        return 0


s = Solution()
a = [
    [".", ".", ".", ".", ".", ".", "p", "."],
    ["p", ".", ".", ".", ".", ".", "R", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "p", "."]]
res = s.numRookCaptures(a)
print(res)
