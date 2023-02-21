class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if mid % 2 == 1:
                if nums[mid] == nums[mid - 1]:
                    l = mid + 1
                else:
                    r = mid
            else:
                if mid + 1 == len(nums):
                    return nums[mid]
                if nums[mid] == nums[mid + 1]:
                    l = mid + 1
                else:
                    r = mid
        return nums[l]
