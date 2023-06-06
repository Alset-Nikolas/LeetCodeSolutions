class StackMaxMin:
    def __init__(self) -> None:
        self.mass = []
        self.mass_max = []
        self.mass_min = []

    def add(self, x):
        if not self.mass:
            self.mass.append(x)
            self.mass_max.append(x)
            self.mass_min.append(x)
            return
        last_item_max = self.mass_max[-1]
        last_item_min = self.mass_min[-1]
        if last_item_max > x:
            self.mass_max.append(last_item_max)
        else:
            self.mass_max.append(x)
        if last_item_min > x:
            self.mass_min.append(x)
        else:
            self.mass_min.append(last_item_min)
        self.mass.append(x)

    def pop(self):
        self.mass.pop()
        self.mass_max.pop()
        self.mass_min.pop()

    def get_max(self):
        return self.mass_max[-1]
    
    def get_min(self):
        return self.mass_min[-1]


class FirstSolution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        stack_min = StackMaxMin()
        stack_max = StackMaxMin()
        for i in range(len(prices)-1, -1, -1):
            x = prices[i]
            stack_max.add(x)
        res = 0     
        for i in range(len(prices)-1):
            x = prices[i]
            stack_max.pop()
            stack_min.add(x)
            min_ = stack_min.get_min()
            max_ = stack_max.get_max()
            print(i, stack_max.mass_max)
            res = max(res, max_ - min_)
        return max(res,0)
    
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_delta = 0
        min_price = prices[0]
        max_price = 0
        for i in range(len(prices)):
            x = prices[i]
            if x < min_price:
                min_price = x
            delta = x - min_price
            max_delta = max(delta, max_delta)
            if x > max_price:
                max_price = x
        return max_delta


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))