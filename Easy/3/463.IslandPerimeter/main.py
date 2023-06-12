from typing import * 

class Solution:
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for i, line_y in enumerate(grid):
            for j, x in enumerate(line_y):
                if x == 1:
                    res += 4
                    if i - 1 >= 0 and grid[i-1][j] == 1:
                        res -= 2
                    if j - 1 >= 0 and grid[i][j-1] == 1:
                        res -= 2
        return res

