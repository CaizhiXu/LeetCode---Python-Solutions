# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
## time - O(n), space - O(1)
class Solution:
    def reverseKGroup(self, head, k):
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        head = dummy
        while head:
            head = self.reverseKnodes(head, k)
        return dummy.next

    def reverseKnodes(self, head, k):
        if not head:
            return None
        newhead = head.next
        last_node = head
        for i in range(k):
            last_node = last_node.next
            if not last_node:
                return None

        prev = last_node.next
        curr = head.next
        while curr != last_node:
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
        curr.next = prev
        head.next = curr
        return newhead