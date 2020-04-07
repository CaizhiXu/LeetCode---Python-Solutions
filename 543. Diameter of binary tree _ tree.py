# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time, space - O(n)
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.depthTree(root)
        return self.res

    def depthTree(self, node):
        if not node:
            return 0
        ldep = self.depthTree(node.left)
        rdep = self.depthTree(node.right)
        self.res = max(self.res, ldep + rdep)
        return max(ldep, rdep) + 1