class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        max_2 = 0
        x = 1
        while x <= right:
            x *= 2
            max_2 += 1 
        good_numbers = [None]*(right+1)
        for j in range(2, max_2+1):
            if good_numbers[j] is None:
                good_numbers[j] = True
                start = 2
                while j*start < right+1:
                    good_numbers[j*start] = False
                    start += 1

        res = 0
        for x in range(left, right+1):
            q = 0
            for b in bin(x)[2:]:
                if b == '1':
                    q += 1
            if q> 1 and good_numbers[q]:
                res += 1
        return res

print(num := 15)
print(num+1)