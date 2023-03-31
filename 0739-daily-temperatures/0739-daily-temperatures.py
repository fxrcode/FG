class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans, s = [0] * len(T), deque()
        for cur in range(len(T) - 1, -1, -1):
            while s and T[s[-1]] <= T[cur]:
                s.pop()
            ans[cur] = s[-1] - cur if s else 0
            s.append(cur)
        return ans