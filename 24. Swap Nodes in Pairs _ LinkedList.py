# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
## time - O(N), space - O(1)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre, curr, nxt = dummy, head, head.next
        while nxt:
            pre.next = nxt
            curr.next = nxt.next
            nxt.next = curr
            pre = curr
            curr = pre.next
            if curr:
                nxt = curr.next
            else:
                break
        return dummy.next