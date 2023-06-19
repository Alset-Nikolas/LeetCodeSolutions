from typing import * 

# Definition for a binary tree node.
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        l = 0

        lwin = 0
        rwin = 1
        nums.append(-1)
        for r in range(1, len(nums)):
            if nums[r-1] >= nums[r]:
                if r-l > rwin - lwin:
                    lwin=l
                    rwin = r
                l=r
        return rwin - lwin


            