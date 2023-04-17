class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        M = max(candies)
        return [candy + extraCandies >= M for candy in candies]