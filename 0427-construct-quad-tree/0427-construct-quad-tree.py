"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def f(top, left, sz):
            if sz == 1:
                return Node(bool(grid[top][left]), True, None, None, None, None)
            half = sz // 2
            right, bottom = left + half, top + half
            kids = [
                f(top, left, half),
                f(top, right, half),
                f(bottom, left, half),
                f(bottom, right, half),
            ]
            if all(k.isLeaf for k in kids) and len(set(k.val for k in kids)) == 1:
                return Node(kids[0].val, True, None, None, None, None)
            else:
                return Node("*", False, *kids)

        return f(0, 0, len(grid))