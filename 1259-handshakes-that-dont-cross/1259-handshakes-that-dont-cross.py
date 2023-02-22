class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        @cache
        def f(n):
            if n == 0:
                return 1
            if n == 2:
                return 1
            x = 0
            for i in range(0, n, 2):
                x += f(i) * f(n - 2 - i)
                x %= 10**9 + 7

            return x

        return f(numPeople)