from typing import *
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        numbers= []
        for h in range(12):
            h_bin = bin(h)[2:]
            h_ones = h_bin.count('1')
            if turnedOn - h_ones >= 0:
                for min in range(60):
                    min_bin = bin(min)[2:]
                    min_ones = min_bin.count('1')
                    if turnedOn - h_ones - min_ones == 0:
                        numbers.append(f'{h}:{min:02}')
        return numbers

                
            
s = Solution()
print(s.readBinaryWatch(1))  