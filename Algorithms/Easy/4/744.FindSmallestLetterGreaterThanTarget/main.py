from typing import *


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        min1 = letters[0]
        i = 0
        while i < len(letters) and target >= letters[i]:
            i += 1
        if i == len(letters):
            return min1
        return letters[i]
