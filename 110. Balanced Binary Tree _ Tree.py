# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## post order, time - O(N), space - O(1)
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        res, dep = self.depth(root)
        return res

    def depth(self, node):
        if not node:
            return True, 0
        l = self.depth(node.left)
        r = self.depth(node.right)
        if not l[0] or not r[0]:
            return False, -1
        if abs(l[1] - r[1]) <= 1:
            return True, max(l[1], r[1]) + 1
        else:
            return False, -1