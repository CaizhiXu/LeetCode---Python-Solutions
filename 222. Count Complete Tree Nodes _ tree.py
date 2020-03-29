# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time - O(logN), space - O(N)
class Solution:
    def __init__(self):
        self.memo = {}

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        h = self.height(root)
        h_right = self.height(root.right)
        if h_right == h - 1:
            return (1 << (h - 1)) + self.countNodes(root.right)
        return (1 << (h - 2)) + self.countNodes(root.left)

    def height(self, node):
        if not node:
            return 0
        if node in self.memo:
            return self.memo[node]
        res = 1 + self.height(node.left)
        self.memo[node] = res
        return res