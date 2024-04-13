from typing import *


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        size_line = len(mat)
        size_clmn = len(mat[0])
        if r * c != size_line * size_clmn:
            return mat

        i_line = 0
        j_clmn = 0
        new_mat = []
        for i in range(r):
            new_line = []
            for j in range(c):
                new_line.append(mat[i_line][j_clmn])

                j_clmn = (j_clmn + 1) % size_clmn
                if j_clmn == 0:
                    i_line = (i_line + 1) % size_line
            new_mat.append(new_line)
        return new_mat
