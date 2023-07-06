from typing import * 
# Definition for singly-linked list.
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        res = 0
        max_line = grid[0]
        for i in range(len(grid)):
            max_item = 0
            for j in range(len(grid[0])):
                if grid[i][j] != 0 :
                    res += 1
                max_line[j] = max(max_line[j], grid[i][j])
                max_item = max(max_item, grid[i][j])
            res += max_item
        res += sum(max_line)
        return res