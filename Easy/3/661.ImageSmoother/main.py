from typing import *


# Definition for a binary tree node.
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        def calc(x, y, img):
            x_min = max(0, x - 1)
            x_max = min(len(img[0]), x + 2)
            y_min = max(0, y - 1)
            y_max = min(len(img), y + 2)
            q = 0
            sum_ = 0
            for x in range(x_min, x_max):
                for y in range(y_min, y_max):
                    sum_ += img[y][x]
                    q += 1
            return int(sum_ / q) if q != 0 else 0

        mass = []
        for y in range(len(img)):
            new_line = []
            for x in range(len(img[0])):
                new_line.append(calc(x, y, img))
            mass.append(new_line)
        return mass


print(Solution().imageSmoother([
    [2, 3, 4],
    [5, 6, 7],
    [8, 9, 10],
    [11, 12, 13],
    [14, 15, 16]
]))
