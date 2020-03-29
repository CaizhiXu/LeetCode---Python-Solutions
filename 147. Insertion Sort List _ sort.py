# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
## time - O(n**2), space - O(1)
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy.next
        while curr.next:
            prev = dummy
            nxt = curr.next
            if nxt.val >= curr.val:
                curr = curr.next
            else:
                while nxt.val > prev.next.val:
                    prev = prev.next
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
        return dummy.next