class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        l, r = 0, 0
        res = 0
        while r < len(nums):
            c = nums[r]
            r += 1
            d[c] += 1
            while l < r and d[c] > k:
                cc = nums[l]
                l += 1
                d[cc] -= 1
            res = max(res, r - l)
        return res