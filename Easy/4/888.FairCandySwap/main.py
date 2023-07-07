from typing import * 
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_a = sum(aliceSizes)
        sum_bob = sum(bobSizes)
        
        if sum_a < sum_bob:
            aliceSizes, bobSizes = bobSizes, aliceSizes
        delta = (sum_a + sum_bob)//2 - min(sum_bob, sum_a)
        aliceSizes.sort()
        bobSizes.sort()
        i = 0
        j = 0
        while i < len(aliceSizes) and j < len(bobSizes):
            if aliceSizes[i] <= bobSizes[j]:
                i += 1
            else:
                if aliceSizes[i] - bobSizes[j] == delta:
                    return [aliceSizes[i], bobSizes[j]] if sum_a > sum_bob else [ bobSizes[j], aliceSizes[i]]
                elif  aliceSizes[i] - bobSizes[j] > delta:
                    j += 1
                else:
                    i += 1
            print(i, j, aliceSizes[i] - bobSizes[j], delta)

 
