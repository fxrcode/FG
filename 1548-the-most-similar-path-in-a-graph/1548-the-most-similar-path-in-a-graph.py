class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        name_to_idx = defaultdict(set)
        for i, name in enumerate(names):
            name_to_idx[name].add(i)
        conn = defaultdict(list)
        for a, b in roads:
            conn[a].append(b)
            conn[b].append(a)
        
        @cache
        def dp(i, length):
            edit = 0 if i in name_to_idx.get(targetPath[-length], [-1]) else 1
            if length == 1:
                return (edit, [i])
            cost, path = min([dp(j, length-1) for j in conn[i]], key=lambda x:x[0])
            return (edit + cost, [i] + path)
        
        
        cost, path = min([dp(i, len(targetPath)) for i in range(n)], key=lambda x:x[0])
        return path