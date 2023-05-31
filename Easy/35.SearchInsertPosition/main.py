class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)
        while r > l:
            m = (l + r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m 
        return l




if __name__ == "__main__":
    s = Solution()
    assert s.searchInsert([1,3,5,6], 5) == 2
    assert s.searchInsert([1,3,5,6], 2) == 1
    assert s.searchInsert([1,3,5,6], 7) == 4