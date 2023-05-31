class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """



if __name__ == "__main__":
    s = Solution()
    assert s.searchInsert('sadbutsad', 'sad') == 0
    assert s.searchInsert('leetcode', 'leeto') == -1
    assert s.searchInsert('mississippi', 'issip') == 4