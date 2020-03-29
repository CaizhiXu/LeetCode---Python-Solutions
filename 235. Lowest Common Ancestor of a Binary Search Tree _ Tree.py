# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## time - O(logN), space - O(1)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if p.val > q.val:
            p, q = q, p
        curr = root
        while curr:
            if p.val <= curr.val and q.val >= curr.val:
                return curr
            if q.val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return None