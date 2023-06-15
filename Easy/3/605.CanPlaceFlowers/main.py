from typing import * 

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res = 0
        for i in range(len(flowerbed)):
            fl = True
            fr = True
            if i -1 >= 0:
                fl = flowerbed[i-1] == 0
            if i + 1 < len(flowerbed):
                fr = flowerbed[i+1] == 0
            if flowerbed[i] == 0 and fl and fr:
                res += 1
                flowerbed[i] = 1
        return n <= res
            