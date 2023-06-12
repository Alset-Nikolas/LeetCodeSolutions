from typing import * 

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        mass = sorted(score)
        res =[]
        info = {
            x:i+1 for i,x in enumerate(mass[::-1])
        }
        for p in score:
            number = info.get(p)
            if number == 1:
                res.append("Gold Medal")
            elif number == 2:
                res.append("Silver Medal")
            elif number == 3:
                res.append("Bronze Medal")
            else:
                res.append(str(number))
        return res