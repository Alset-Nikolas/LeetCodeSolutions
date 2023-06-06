class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        last_row = []
        for i in range(rowIndex+1):
            if i == 0:
                last_row = [1]
                continue
            new_row = [1 for x in range(len(last_row)+1)]
            for j in range(1, len(new_row)-1):
                x1 = last_row[j-1]
                x2 = last_row[j]
                new_row[j] = x1+x2
            last_row = new_row
        return last_row
