# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        mn = float("inf")
        prev: Optional[TreeNode] = None

        def ino(T: TreeNode):
            if not T:
                return 
            ino(T.left)
            nonlocal prev, mn
            if prev:
                mn = min(mn, T.val - prev.val)
            prev = T
            ino(T.right)

        ino(root)
        return mn