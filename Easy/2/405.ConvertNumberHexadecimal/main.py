from typing import *
# Definition for a binary tree node.
def twos_complement(n, bits=32):
    mask = (1 << bits) -1
    if n < 0:
        n = ((abs(n) ^ mask) + 1)
    return bin(n & mask)
 

class Solution:
    info = {
        10: "a",
        11: "b",
        12: "c",
        13: "d",
        14: "e",
        15: "f"
    }
    def toHex(self, num: int) -> str:
        num = int(twos_complement(num), 2)
        if num == 0:
            return '0'
        res = []
        while num > 0:
            x = num%16
            if x > 9:
                x = self.info[x]
            res.append(str(x))
            num = num >> 4
        return ''.join(res[::-1])

print(Solution().toHex(26))

