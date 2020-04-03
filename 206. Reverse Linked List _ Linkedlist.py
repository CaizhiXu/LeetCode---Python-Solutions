# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## time - O(N), space - O(1)
class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev, curr = None, head
        nxt = curr.next
        while nxt:
            curr.next = prev
            prev, curr = curr, nxt
            nxt = nxt.next
        curr.next = prev
        return curr


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## time, space - O(N)
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        nxt_node = head.next
        new_head = self.reverseList(nxt_node)
        nxt_node.next = head
        head.next = None
        return new_head