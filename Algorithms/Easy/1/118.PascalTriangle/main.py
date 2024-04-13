class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            if i == 0:
                res.append([1])
                continue
            last_row = res[-1]
            item = [1 for x in range(len(last_row) + 1)]
            for j in range(1, len(item) - 1):
                x1 = last_row[j - 1]
                x2 = last_row[j]
                item[j] = x1 + x2
            res.append(item)
        return res
