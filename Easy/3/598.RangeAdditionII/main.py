from typing import * 
# Definition for a Node.
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        matr = [[0 for y in range(m)] for x in range(n)]
        res = 0
        res_max = 0
        for x, y in ops:
            for yj in range(y):
                for xi in range(x):
                    matr[xi][yj] +=1
                    new_variant = matr[xi][yj]
                    if res_max < new_variant:
                        res_max = new_variant
                        res = 1
                    elif new_variant == res_max:
                        res += 1


        return res
print(Solution().maxCount(3, 3, [[2,2],[3,3]]))