from typing import * 
import string
import math

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        if len(image) == 0:
            return image
        N = len(image)
        for j in range(N):
            for i in range(N):
                image[j][i] = int(not bool(image[j][i]))
            image[j] = image[j][::-1]
        return image
    