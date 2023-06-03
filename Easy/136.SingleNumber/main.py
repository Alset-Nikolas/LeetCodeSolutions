class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set()
        for x in nums:
            if x in num_set:
                num_set.remove(x)
            else:
                num_set.add(x)
        return num_set.pop()