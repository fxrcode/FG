"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(u: Node) -> Node:
            """[summary]
            Runtime: 55 ms, faster than 49.83% of Python3 online submissions for Clone Graph.

            T: O(E)
            """

            if not u:
                return u
            if u in mp:  # if found, then it must have cloned subgraph
                return mp[u]
            mp[u] = Node(u.val)
            for v in u.neighbors:
                mp[u].neighbors.append(dfs(v))
            return mp[u]

        mp = {}
        return dfs(node)