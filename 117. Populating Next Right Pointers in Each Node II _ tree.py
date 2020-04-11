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

        while head:
            new_head, curr = None, None
            while head:
                if head.left:
                    if not new_head:
                        new_head = head.left
                        curr = head.left
                    else:
                        curr.next = head.left
                        curr = curr.next
                if head.right:
                    if not new_head:
                        new_head = head.right
                        curr = head.right
                    else:
                        curr.next = head.right
                        curr = curr.next
                head = head.next
            if curr:
                curr.next = None
            head = new_head
        return root