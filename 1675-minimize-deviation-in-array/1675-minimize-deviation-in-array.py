class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        mn = 2e9
        evens = []
        mnmxdev = 2e9
        for n in nums:
            if n % 2 == 1:
                n *= 2
            heappush(evens, -n)
            mn = min(n, mn)
        while evens:
            mx = -heappop(evens)
            mnmxdev = min(mnmxdev, abs(mx - mn))
            if mx % 2 == 1:
                break
            div2 = mx // 2
            heappush(evens, -div2)
            # ? Q: what if div2 is the mn? A: it's fine. div2 will substitute the mn
            mn = min(mn, div2)
        return mnmxdev