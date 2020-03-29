"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
## time, space - O(n)
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                for chi in node.children[::-1]:
                    stack.append(chi)
        return res