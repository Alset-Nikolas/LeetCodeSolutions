class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        res = ''
        ans = []
        for x in nums:
            res = res + str(x)
            res_10 = int(res, 10)
            ans.append(res_10 % 5 == 0)
        return ans
