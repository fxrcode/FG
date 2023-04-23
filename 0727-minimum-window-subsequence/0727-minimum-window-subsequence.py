class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        @cache
        def dfs(i, j):
            if j == len(s2):
                return i

            ind = s1.find(s2[j], i + 1)
            return float("inf") if ind == -1 else dfs(ind, j + 1)

        l, res = float("inf"), ""
        for i, s in enumerate(s1):
            if s == s2[0]:
                j = dfs(i, 1)
                if j - i < l:
                    l, res = j - i, s1[i : j + 1]
        return res