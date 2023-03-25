class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def union(x: int, y: int) -> None:
            def find(x: int) -> int:
                while x != id[x]:     # if x is not root, keep tracing the root.
                    id[x] = id[id[x]] # Path compression.
                    x = id[x]         # trace root.
                return x              # Root found.
    
            rx, ry = map(find, (x, y)) # Find the roots of x and y. 
            if rx != ry:               # Different roots means there are not in same group. 
                # Merge smaller group into bigger group. => Weighted Quick Union.
                if sz[rx] > sz[ry]:
                    sz[rx] += sz[ry]
                    id[ry] = id[rx]
                    roots.discard(ry) # smaller group root removed after union.
                else:
                    id[rx] = id[ry]
                    sz[ry] += sz[rx]
                    roots.discard(rx)
                    
        id = list(range(n)) # Initialize the root of each vertex as itself.
        sz = [1] * n        # Initialize the size of each group as 1.
        roots = {*range(n)} # Initialize the root of each vertex as itself.
        for a, b in edges:
            union(a, b)     # Perform Union Find.
        pairs = 0    
        for r in roots:     # Traverse roots.
            n -= sz[r]      # Number of the total size of non-visited groups.
            pairs += n * sz[r] # Add the pairs between group r and non-visited groups.
        return pairs