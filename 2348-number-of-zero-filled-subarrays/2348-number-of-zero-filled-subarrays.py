class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt = zeroSubarraysEndingAtCurrentIndex = 0
        for num in nums:
            if num == 0:
                zeroSubarraysEndingAtCurrentIndex += 1
                cnt += zeroSubarraysEndingAtCurrentIndex
            else:
                zeroSubarraysEndingAtCurrentIndex = 0
        return cnt