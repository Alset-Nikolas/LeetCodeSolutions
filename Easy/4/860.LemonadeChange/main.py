from typing import * 

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bank = dict()
        for x in bills:
            if x == 5:
                if x not in bank:
                    bank[5] = 0
                bank[5] += 1
            elif x == 10:
                if 5 not in bank or bank[5] <= 0:
                    return False
                bank[5] -= 1
                if 10 not in bank:
                    bank[10] = 0
                bank[10] += 1
            else:
                if 5 not in bank:
                    return False
                if 10 not in bank or bank[10]<=0:
                    if bank[5] < 3:
                        return False
                    bank[5] -= 3
                    continue
                if bank[5] <= 0:
                    return False
                bank[5] -= 1
                bank[10] -= 1
        return True                