from typing import * 
import string
import math

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x11, y11, x12, y12 = rec1
        x21, y21, x22, y22 = rec2
        return min(y22, y12) > max(y11, y21) and min(x12, x22) > max(x11, x21)