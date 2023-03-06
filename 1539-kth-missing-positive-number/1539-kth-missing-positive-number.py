class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m] - (m + 1) >= k:
                r = m
            else:
                l = m + 1
        print(l, r)
        return l + k 