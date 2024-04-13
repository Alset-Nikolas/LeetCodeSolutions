class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        res = []
        matr = [[0 for x in range(cols)] for y in range(rows) ]
        def go(x, y):
            steck = [[y, x]]
            param = 1
            while steck != []:
                y_, x_ = steck.pop()
                if not 0<=x_<cols:
                    continue
                if not 0 <=y_<rows:
                    continue
                if matr[y_][x_] != 0:
                    continue

                matr[y][x] = param
                res.append([y, x])
                go(x-1, y, param+1)
                go(x+1, y, param+1)
                go(x, y-1, param+1)
                go(x, y+1, param+1)
        go(cCenter, rCenter)
        return res

if __name__ == '__main__':

    s=  Solution()
    res = s.allCellsDistOrder(2, 2, 0, 1)
    print(res)