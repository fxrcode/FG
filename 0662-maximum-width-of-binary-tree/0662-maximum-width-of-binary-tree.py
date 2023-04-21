# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        di = defaultdict(list)

        def dfs(node, level, column):
            if node:
                di[level].append(column)
                dfs(node.left, level + 1, column * 2)
                dfs(node.right, level + 1, column * 2 + 1)

        dfs(root, 0, 0)
        return max([max(di[level]) - min(di[level]) + 1 for level in di])