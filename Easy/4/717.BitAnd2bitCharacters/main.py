from typing import *


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        i = 0
        while i < len(bits):
            if bits[i] == 0:
                i += 1
                flag = True
            else:
                i += 2
                flag = False
        return flag
