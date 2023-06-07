class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return len(set(ransomNote)) == len(set(magazine)) == len(set(zip(ransomNote,magazine))) and set(ransomNote) == set(magazine)