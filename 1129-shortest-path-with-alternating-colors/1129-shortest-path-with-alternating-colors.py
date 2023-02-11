class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        neighbors = [[[], []] for _ in range(n)]
        ans = [[0, 0]]+[[2*n, 2*n] for _ in range(n-1)]
        for u, v in redEdges: neighbors[u][0].append(v)
        for u, v in blueEdges: neighbors[u][1].append(v)
        
        def dfs(u, c, dist):
            for v in neighbors[u][c]:
                if dist+1<ans[v][c]:
                    ans[v][c] = dist+1
                    dfs(v, 1-c, dist+1)
                    
        dfs(0, 0, 0)
        dfs(0, 1, 0)
        return [x if x<2*n else -1 for x in map(min, ans)]