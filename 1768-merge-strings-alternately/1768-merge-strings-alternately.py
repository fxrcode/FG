class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for i in range(min(len(word1), len(word2))):
            res.append(word1[i] + word2[i])
        # !for i in range(5). i=4 after loop! So I need to word1[i+1:] rather word1[i:]
        res.append(word1[i + 1 :] + word2[i + 1 :])
        return "".join(res)