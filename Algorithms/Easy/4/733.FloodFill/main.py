from typing import *


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def go(image: List[List[int]], sr: int, sc: int, color: int, porog):
            if not len(image) > sr >= 0:
                return
            if not len(image[-1]) > sc >= 0:
                return
            if image[sr][sc] != porog or image[sr][sc] == color:
                return

            image[sr][sc] = color

            go(image, sr - 1, sc, color, porog)
            go(image, sr + 1, sc, color, porog)
            go(image, sr, sc - 1, color, porog)
            go(image, sr, sc + 1, color, porog)

        go(image, sr, sc, color, image[sr][sc])
        return image


print(Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
