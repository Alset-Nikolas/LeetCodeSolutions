from typing import * 
import string

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        info = dict()
        max_size = 0
        ans = None
        banned_set = set(banned)
        for x in string.punctuation:
            paragraph=paragraph.replace(x, ' ')
        for slovo in paragraph.split():
            slovo = slovo.lower()
            if slovo not in info:
                info[slovo] = 0
            info[slovo] += 1
            if  info[slovo] > max_size and slovo not in banned_set:
                max_size = info[slovo]
                ans = slovo
        return ans
