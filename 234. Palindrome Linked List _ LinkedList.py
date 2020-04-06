# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
## time - O(n), space - O(1)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
        head2 = prev
        while head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True