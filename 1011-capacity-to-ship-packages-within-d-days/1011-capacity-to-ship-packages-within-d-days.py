class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity) -> bool:
            """
            https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/769698/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.
            zhijun_liao feasible is more cleaner than mine
            """
            d = 1
            tot = 0
            for w in weights:
                tot += w
                if tot > capacity:  # too heavy, wait for the next day
                    tot = w
                    d += 1
                    if d > days:  # cannot ship within D days
                        return False
            return True
        
        l, r = max(weights), sum(weights) + 1
        while l < r:
            m = (l + r) // 2
            if feasible(m):
                r = m
            else:
                l = m + 1
        return l