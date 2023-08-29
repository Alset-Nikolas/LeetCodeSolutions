class Solution:
    def __get_freq_el(self, text: str) -> dict:
        res = dict()
        for x in text:
            if x not in res:
                res[x] = 0
            res[x] += 1
        return res

    def isAnagram(self, s: str, t: str) -> bool:
        return self.__get_freq_el(s) == self.__get_freq_el(t)
