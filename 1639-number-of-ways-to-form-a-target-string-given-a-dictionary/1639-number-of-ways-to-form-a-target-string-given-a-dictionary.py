class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if j >= len(target):
                return 1
            k = len(cnt) - len(target) + j + 1
            return (
                sum(cnt[k][target[j]] * dfs(k + 1, j + 1) for k in range(i, k))
                % 1000000007
            )

        cnt = [Counter(w[i] for w in words) for i in range(len(words[0]))]
        return dfs(0, 0)