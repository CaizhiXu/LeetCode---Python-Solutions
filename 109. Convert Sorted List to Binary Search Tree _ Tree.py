# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time - O(nlogn), space - O(n)
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        slow, fast = head, head.next
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        if slow.next:
            head2 = slow.next.next
            root = TreeNode(slow.next.val)
            slow.next = None
            root.left = self.sortedListToBST(head)
            root.right = self.sortedListToBST(head2)
        else:
            root = TreeNode(slow.val)
        return root