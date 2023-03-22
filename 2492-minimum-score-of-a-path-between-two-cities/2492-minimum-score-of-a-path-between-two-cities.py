class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        T = Hashable
        Dist = int | float
        Graph = Mapping[T, Mapping[T, Dist]]

        def min_dist(graph: Graph, u: T, seen: set[T]) -> Dist:
            return (
                (
                    seen.add(u)
                    or min(
                        min(d, min_dist(graph, v, seen))
                        for v, d in graph[u].items()
                    )
                )
                if u not in seen
                else inf
            )

        g = defaultdict(dict)
        for u, v, d in roads:
            g[u][v] = g[v][u] = d

        return min_dist(g, 1, set())