class Solution:
    def partitionString(self, s: str) -> int:
        cur = set()
        res = 1
        
        for c in s:
            if c in cur:
                cur = set()
                res += 1
            cur.add(c)
                
        return res