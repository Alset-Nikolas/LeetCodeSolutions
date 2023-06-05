class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        porog = len(nums) // 2
        numbers_freq = dict()
        for x in nums:
            if x not in numbers_freq:
                numbers_freq[x] = 0
            numbers_freq[x] += 1
            if numbers_freq[x] > porog:
                return x
        return
