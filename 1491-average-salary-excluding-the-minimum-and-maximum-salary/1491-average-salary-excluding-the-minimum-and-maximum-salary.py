class Solution:
    def average(self, salary: List[int]) -> float:
        mn, mx, tot = float("inf"), 0, 0
        for s in salary:
            mn = min(mn, s)
            mx = max(mx, s)
            tot += s
        return (tot - mn - mx) / (len(salary) - 2)