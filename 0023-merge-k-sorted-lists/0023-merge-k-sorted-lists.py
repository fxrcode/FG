# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(lists):
            sz = len(lists)
            if not sz:
                return None
            if sz == 1:
                return lists[0]

            mid = sz // 2
            l, r = map(merge, [lists[:mid], lists[mid:]])
            return merge2lists(l, r)

        def merge2lists(l1, l2):
            dummy = end = ListNode(None)
            while l1 and l2:
                if l1.val <= l2.val:
                    end.next = l1
                    l1 = l1.next
                else:
                    end.next = l2
                    l2 = l2.next
                end = end.next
            end.next = l1 or l2
            return dummy.next

        return merge(lists)