class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cost = 0
        last7 = deque()
        last30 = deque()
        for d in days:
            while last7 and last7[0][0] + 7 <= d:
                last7.popleft()
            while last30 and last30[0][0] + 30 <= d:
                last30.popleft()
            last7.append((d, cost + costs[1]))
            last30.append((d, cost + costs[2]))
            cost = min(cost + costs[0], last7[0][1], last30[0][1])
        return cost