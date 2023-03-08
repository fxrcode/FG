class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def f(x: int) -> bool:
            """
            math.ceil is quite handy!
            if p < x, then p/x < 1, so ceil => 1
            if p >= x, say p/x = 2.5, then ceil => 3
            """
            hr = 0
            for p in piles:
                hr += ceil(p / x)
            return hr <= h

        l, r = 1, max(piles)
        while l < r:
            x = (l + r) // 2
            # zhijun_liao: Powerful Ultimate Binary Search Template: Minimize k, s.t. f(k) is True
            #  f(k) map problem to FFFTTT, find first index of T
            if f(x):
                r = x
            else:
                l = x + 1
        return l