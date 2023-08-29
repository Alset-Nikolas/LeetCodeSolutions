class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        return len(set(x for x in pattern)) == len(set(s_list)) == len(set(zip(pattern, s_list))) and len(
            pattern) == len(s_list)
