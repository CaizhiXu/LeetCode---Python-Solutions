# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
## time - O(N), space - O(1)
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        prev, curr, nxt = dummy, head, head.next
        cnt = 1
        while cnt < m:
            cnt += 1
            prev, curr = curr, curr.next
            nxt = curr.next

        tail = prev
        end = curr
        prev = None
        while cnt <= n:
            curr.next = prev
            prev, curr = curr, nxt
            if nxt:
                nxt = nxt.next
            cnt += 1
        tail.next = prev
        end.next = curr
        return dummy.next