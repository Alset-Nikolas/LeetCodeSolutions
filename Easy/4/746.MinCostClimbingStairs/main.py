from typing import * 

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # F(i) = min(F(i-1), F(i-2)) + c(i)
        cost.append(0)
        cost.append(0)
        F = []
        for i in range(len(cost)):
            ci = cost[i]
            v1 = F[i-1] if i - 1 >= 0 else 0
            v2 = F[i-2] if i -2 >= 0 else 0
            F.append(ci+min(v1,v2))
    
        return min(F[-1], F[-2])