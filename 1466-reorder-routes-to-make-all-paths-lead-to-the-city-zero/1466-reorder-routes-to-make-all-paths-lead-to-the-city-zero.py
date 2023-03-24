class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(start):
            nonlocal visited, count
            visited[start] = 1
            for neib in adj[start]:
                if visited[neib[0]] == 0:
                    if neib[1] == 1:
                        count += 1
                    dfs(neib[0])
    
        visited = [0] * n
        adj = defaultdict(list) 
        count = 0
        for i, j in connections:
            adj[i].append([j,1])
            adj[j].append([i,-1])

        dfs(0)
        return count