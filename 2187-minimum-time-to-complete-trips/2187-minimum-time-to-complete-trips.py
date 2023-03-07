class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        lo, hi = 0, 10 ** 14
        while lo < hi:
            need = lo + (hi - lo) // 2
            trips = sum(need // t for t in time)
            if trips < totalTrips:
                lo = need + 1
            else:
                hi = need
        return lo