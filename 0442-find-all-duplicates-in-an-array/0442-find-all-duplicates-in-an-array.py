class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        bk = [0] * (len(nums) + 1)
        res = []
        for v in nums:
            bk[v] += 1
        for i, v in enumerate(bk):
            if v == 2:
                res.append(i)
        return res
