class Solution:
    def reverseVowels(self, s: str) -> str:
        s = [x for x in s]
        j = len(s)-1
        for i in range(len(s)):
            if s[i].lower() in {'a', 'e', 'i', 'o', 'u'}:
                while j >0 and j >i and s[j].lower() not in {'a', 'e', 'i', 'o', 'u'}:
                    j -= 1
                if s[j].lower() in {'a', 'e', 'i', 'o', 'u'}:
                    s[i], s[j] = s[j], s[i]
                    j -= 1
            if j <= i:
                break
        return ''.join(s)
print(Solution().reverseVowels('ai'))