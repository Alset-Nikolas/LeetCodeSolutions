from typing import *


class Solution:
    def get_freq_items(self, test: str):
        q = dict()
        for x in test:
            if x not in q:
                q[x] = 0
            q[x] += 1
        return q

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        q1 = self.get_freq_items(nums1)
        q2 = self.get_freq_items(nums2)
        res = []
        for k, v in q1.items():
            if k in q2:
                res += [k] * min(q1[k], q2[k])
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.intersect([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    assert s.intersect([1, 1, 1], [1, 1, 1]) == [1, 1, 1]
    assert s.intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]
