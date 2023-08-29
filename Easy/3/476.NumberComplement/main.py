class Solution:
    def findComplement(self, num: int) -> int:
        print(bin((1 << (len(bin(num)[2:]))) - 1))

        return (1 << len(bin(num)[2:])) - 1 - num


print(Solution().findComplement(1))
