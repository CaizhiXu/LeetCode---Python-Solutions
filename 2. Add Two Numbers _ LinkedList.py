# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
## time, space - O(m + n)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        head = dummy
        carry = 0
        while l1 and l2:
            val = (carry + l1.val + l2.val)%10
            carry = (carry + l1.val + l2.val)//10
            head.next = ListNode(val)
            head = head.next
            l1 = l1.next
            l2 = l2.next
        node = l1 or l2
        while node:
            val = (carry + node.val)%10
            carry = (carry + node.val)//10
            head.next = ListNode(val)
            head = head.next
            node = node.next
        if carry:
            head.next = ListNode(carry)
            head = head.next
        head.next = None
        return dummy.next