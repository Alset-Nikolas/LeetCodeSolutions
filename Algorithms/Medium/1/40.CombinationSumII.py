class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []

        def go_step(slice_candidates, sum_):
            if sum_ < 0:
                return
            slice_res = []
            last_x = None
            i = 0
            while i < len(slice_candidates):
                x = slice_candidates[i]
                if sum_ - x > 0:
                    res_slice = go_step(slice_candidates[i + 1:], sum_ - x)
                    for item in res_slice:
                        slice_res.append([x] + item)
                    last_x = slice_candidates[i]
                elif sum_ - x == 0:
                    slice_res.append([x])
                    last_x = slice_candidates[i]
                i += 1
                while last_x and i < len(slice_candidates) and slice_candidates[i] == last_x:
                    i += 1

            return slice_res

        return go_step(candidates, target)
