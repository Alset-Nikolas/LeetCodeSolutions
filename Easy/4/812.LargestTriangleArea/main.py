from typing import *


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        s = 0
        for i in range(len(points)):
            for j in range(len(points)):
                for k in range(len(points)):
                    if len(set([i, j, k])) < 3:
                        continue
                    li_calc = lambda point1, point2: ((point1[0] - point2[0]) ** 2 + (
                                point1[1] - point2[1]) ** 2) ** 0.5
                    li = li_calc(points[i], points[j])
                    lk = li_calc(points[i], points[k])
                    lj = li_calc(points[j], points[k])
                    p = (li + lj + lk) / 2
                    if p * (p - li) * (p - lj) * (p - lk) > 0:
                        si = (p * (p - li) * (p - lj) * (p - lk)) ** 0.5
                        s = max(s, (p * (p - li) * (p - lj) * (p - lk)) ** 0.5)
        return s
