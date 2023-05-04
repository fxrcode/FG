class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R = deque(i for i, x in enumerate(senate) if x == 'R')
        D = deque(i for i, x in enumerate(senate) if x == 'D')
        
        while R and D:
            r, d = R.popleft(), D.popleft()
            if r < d:
                R += r + len(senate),
            else:
                D += d + len(senate),
        
        return R and 'Radiant' or 'Dire'