class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        res = []
        for i, s in enumerate(sentence.split()):
            news = s
            if any(s.lower().startswith(x) for x in ['a', 'e', 'i', 'o', 'u']):
                news = news + 'ma'
            else:
                q = news[0]
                news = news[1:] + q + 'ma'

            news = news + 'a' * (i + 1)

            res.append(news)
        return ' '.join(res)
