class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = set()
        while True:
            n_next = 0
            for x in str(n):
                n_next += int(x) * int(x)
            if n_next not in numbers:
                numbers.add(n_next)
            else:
                return n_next == 1
            n = n_next
