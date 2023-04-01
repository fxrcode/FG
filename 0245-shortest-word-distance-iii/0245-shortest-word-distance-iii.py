class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        n = len(wordsDict)
        minimum = n
        w1 = -1
        w2 = -1
        for i in range(n):
            if wordsDict[i] == word1:
                w1 = i
                if w2 != -1:
                    minimum = min(w1 - w2, minimum)
            if wordsDict[i] == word2:
                w2 = i
                if w1 != -1 and w1 != w2:
                    minimum = min(w2 - w1, minimum)
        return minimum