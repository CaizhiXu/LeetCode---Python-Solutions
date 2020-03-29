# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        return self.dfs(root)

    def dfs(self, node):
        if not node:
            return 0
        return max(self.dfs(node.left), self.dfs(node.right)) + 1