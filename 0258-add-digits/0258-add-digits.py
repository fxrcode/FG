class Solution:
    def addDigits(self, x: int) -> int:
        if x == 0: return x
        return 9 if x % 9 == 0 else x % 9