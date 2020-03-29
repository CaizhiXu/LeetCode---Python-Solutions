# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time, space ~ O(nlogn)
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        if not s:
            return False
        return int(self.traverse(s, t)) + int(self.isSubtree(s.left, t)) + int(self.isSubtree(s.right, t))

    def traverse(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return self.traverse(s.left, t.left) and self.traverse(s.right, t.right)