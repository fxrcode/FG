class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        out = -1
        n = len(edges)
        visited = set()

        def dfs(node, edges, dist):
            nonlocal out
            visited.add(node)
            neighbor = edges[node]

            if neighbor != -1 and neighbor not in visited:
                dist[neighbor] = dist[node] + 1
                dfs(neighbor, edges, dist)
            elif neighbor != -1 and neighbor in dist:
                out = max(out, dist[node] - dist[neighbor] + 1)

        for i in range(n):
            if i not in visited:
                dist = dict()
                dist[i] = 1
                dfs(i, edges, dist)

        return out