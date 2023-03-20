class Solution:
    def canPlaceFlowers(self, F: List[int], n: int) -> bool:
        count = 0
        F = [0] + F + [0]
        for i in range(1, len(F) - 1):
            if F[i - 1] + F[i] + F[i + 1] == 0:
                F[i] = 1
                count += 1
                if count >= n:
                    return True
        return count >= n