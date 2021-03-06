class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq, n, ans = deque(), len(nums), []
        for i in range(n):
            while deq and deq[0] <= i-k:
                deq.popleft()
            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()
            deq.append(i)
            
            ans.append(nums[deq[0]])
            
        return ans[k-1:]