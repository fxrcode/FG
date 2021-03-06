# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None
        q = deque([root])
        while q:
            qlen = len(q)
            for i in range(qlen):
                cur = q.popleft()
                if cur == u:
                    return q.popleft() if i != qlen - 1 else None
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)