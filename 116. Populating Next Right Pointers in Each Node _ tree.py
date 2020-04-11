"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
## time - O(n), space - O(1)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        root.next = None
        head = root
        while head.left:
            new_head = head.left
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                else:
                    head.right.next = None
                head = head.next
            head = new_head
        return root