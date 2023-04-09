class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        G = defaultdict(list)
        vis = [0] * len(colors)
        for i in edges:
            G[i[0]].append(i[1])
        know = {}

        def dfs(node, x):
            if node in know:
                return know[node]
            vis[node] = 1
            dic = defaultdict(int)
            x.add(node)
            # mx=max(mx,dic[colors[node]])
            for i in G[node]:
                if i in x:
                    know[node] = -1
                    return -1
                else:
                    p = dfs(i, x)
                    if p == -1:
                        know[node] = -1
                        return -1
                    else:
                        for i in p.keys():
                            dic[i] = max(dic[i], p[i])
            x.remove(node)
            dic[colors[node]] += 1
            know[node] = dic
            return dic

        mx = 0
        for b in range(len(colors)):
            if vis[b] == 0:
                s = set()
                ans = dfs(b, s)
                if ans == -1:
                    return -1
                else:
                    for i in ans.values():
                        mx = max(mx, i)
        return mx