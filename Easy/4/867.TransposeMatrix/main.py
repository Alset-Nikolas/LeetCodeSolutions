from typing import * 
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n,m = len(matrix), len(matrix[0])
        matr = [[0 for x in range(n)] for y in range(m)]
        for i in range(n):
            for j in range(m):
                matr[j][i] = matrix[i][j]
        return matr