class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        heap = []
        projects = sorted(zip(Profits, Capital), key=lambda l: l[1])
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][1] <= W:
                heapq.heappush(heap, -projects[i][0])
                i += 1
            if heap: W -= heapq.heappop(heap)
        return W