# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
## time - O(n), space - O(1)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        first, second = dummy, dummy
        for i in range(n):
            second = second.next
        while second.next:
            second = second.next
            first = first.next
        first.next = first.next.next
        return dummy.next