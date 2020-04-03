# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, p: ListNode, q: ListNode) -> ListNode:
        dummy = ListNode(-1)
        head = dummy
        while p and q:
            if p.val < q.val:
                head.next = p
                p = p.next
            else:
                head.next = q
                q = q.next
            head = head.next
        head.next = p or q
        return dummy.next
