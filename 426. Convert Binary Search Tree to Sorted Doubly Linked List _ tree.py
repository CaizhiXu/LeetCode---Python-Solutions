"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


## time - O(n), space - O(h)
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        stack, curr = [], root
        self.inorder_left(curr, stack)
        head = stack.pop()
        prev = head
        self.inorder_left(prev.right, stack)
        while stack:
            curr = stack.pop()
            self.inorder_left(curr.right, stack)
            prev.right = curr
            curr.left = prev
            prev = curr
        curr.right = head
        head.left = curr
        return head

    def inorder_left(self, node, stack):
        while node:
            stack.append(node)
            node = node.left