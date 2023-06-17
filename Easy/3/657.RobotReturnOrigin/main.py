from typing import * 

# Definition for a binary tree node.
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x2 = 0
        y2 = 0
        for x in moves:
            if x == 'U':
                y2 -= 1
            elif x == 'D':
                y2 += 1
            elif x == 'L':
                x2 -= 1
            elif x == 'R':
                x2 += 1
        return x2==0 and y2 == 0
        