class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        cum_sum = maximum = 0

        for i, num in enumerate(nums, start=1):
            cum_sum += num
			# At each step, we can try to minimize the element by evenly placing
			# the excess between the previous elements.
            maximum = max(ceil(cum_sum / i), maximum)

        return maximum