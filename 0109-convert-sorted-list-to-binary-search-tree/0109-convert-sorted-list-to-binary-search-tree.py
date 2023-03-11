# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def helper(beg, end):
            if beg > end: return None
            mid = (beg + end)//2
            left = helper(beg, mid - 1)
            root = TreeNode(self.head.val)
            self.head = self.head.next
            root.left = left
            root.right = helper(mid + 1, end)
            return root
        
        self.head, copy, n = head, head, 0
        while copy:
            copy = copy.next
            n += 1
            
        return helper(0, n-1)