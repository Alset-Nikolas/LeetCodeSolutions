from typing import * 
import heapq

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        heap = []
        for i, x in enumerate(nums):
            if len(heap) > 1 and heap[0][0] >= x:
                continue
            heapq.heappush(heap, [x, i])
            if len(heap) > 2:
                heapq.heappop(heap)
            
        if len(heap) != 2:
            return -1
        max_element = heap[1][0]
        mex_index = heap[1][1] 
        return mex_index if max_element >= heap[0][0]*2 else -1 
print(Solution().dominantIndex([1,2,3,4]))