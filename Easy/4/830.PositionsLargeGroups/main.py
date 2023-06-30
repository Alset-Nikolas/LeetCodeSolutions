from typing import * 
import string
import math

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        if s == '':
            return []
        res = []
        i = 0
        j=0
        for j in range(1, len(s)):
            if s[i] != s[j]:
                if j - i >= 3:
                    res.append([i, j-1])
                i = j
        if j - i >= 2:
            res.append([i, j])
            
        return res