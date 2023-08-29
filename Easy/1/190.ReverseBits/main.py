class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n: int) -> int:
        n_str = bin(n)[2:]

        return int('0b' + n_str[::-1] + '0' * (32 - len(n_str)), 2)


if __name__ == "__main__":
    s = Solution()
    n = 43261596
    # n_32b='{:032b}'.format(n)
    assert s.reverseBits(n) == 964176192
