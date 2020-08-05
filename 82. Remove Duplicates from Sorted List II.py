# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
## time - O(n), space - O(1)
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head

        pre, curr = dummy, head
        while curr and curr.next:
            if curr.val != curr.next.val:
                pre, curr = curr, curr.next
            else:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                pre.next = curr.next
                curr = curr.next
        return dummy.next