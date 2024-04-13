class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = int(''.join(str(x) for x in digits)) + 1
        return [int(x) for x in str(number)]
