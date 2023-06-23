from typing import * 
import string

# Definition for a binary tree node.
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        info ={'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}
        res = set()
        for w in words:
            w_morse = ''.join([info[x] for x in w])
            res.add(w_morse)
        return len(res)