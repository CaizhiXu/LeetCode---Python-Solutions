# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time, space - O(N)
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.res = 0
        if not root:
            return 0
        self.postOrder(root)
        return self.res

    def postOrder(self, node):
        if not node:
            return True
        if not node.left and not node.right:
            self.res += 1
            return True
        l = self.postOrder(node.left)
        r = self.postOrder(node.right)
        if not l or not r:
            return False
        if node.left and node.left.val != node.val:
            return False
        if node.right and node.right.val != node.val:
            return False
        self.res += 1
        return True