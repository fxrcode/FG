class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        self.id, self.count = list(range(n)), n
        
        def union(x: int, y: int) -> None:
            
            def find(x: int) -> int:
                while x != self.id[x]:
                    x = self.id[x]
                return x   

            rx, ry = find(x), find(y)
            if rx == ry:
                return
            self.id[rx] = ry
            self.count -= 1
        
        for c1, c2 in connections:
            union(c1, c2)
        return -1 if len(connections) < n - 1 else self.count - 1