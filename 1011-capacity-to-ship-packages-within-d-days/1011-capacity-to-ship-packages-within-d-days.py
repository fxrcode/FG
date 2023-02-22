class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(x):
            c = 0
            d = 1
            for w in weights:
                if c + w > x:
                    c = w
                    d += 1
                else:
                    c += w
                if d > days:
                    return False
            if d <= days:
                return True
            return False

        l, r = max(weights), sum(weights) + 1
        while l < r:
            m = (l + r) // 2
            if feasible(m):
                r = m
            else:
                l = m + 1
        return l