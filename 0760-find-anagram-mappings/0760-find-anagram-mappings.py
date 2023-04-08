class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(deque)
        for i, v in enumerate(nums2):
            d[v].append(i)
        ans = []
        for v in nums1:
            ans.append(d[v].popleft())
        return ans