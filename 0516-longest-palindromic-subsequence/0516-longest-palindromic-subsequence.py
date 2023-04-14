class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        @cache
        def dp(l, r):
            if l > r:
                return 0
            if l == r:
                return 1
            if s[l] == s[r]:
                return dp(l + 1, r - 1) + 2
            return max(dp(l, r - 1), dp(l + 1, r))

            # XXX: why considering these 2? because that's subproblem of current problem (l,r)
            # BUG: don't add 1, because we're directly checking sub-problem!
            # return max(dp(l, r-1), dp(l+1, r))+1

        return dp(0, n - 1)