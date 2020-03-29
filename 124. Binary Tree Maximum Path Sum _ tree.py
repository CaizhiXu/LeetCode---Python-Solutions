# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time, space - O(N)
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.maxSum = -float('inf')
        self.maxPathSum_withRoot(root)
        return self.maxSum

    def maxPathSum_withRoot(self, node):
        if not node:
            return 0
        l = self.maxPathSum_withRoot(node.left)
        r = self.maxPathSum_withRoot(node.right)
        self.maxSum = max(self.maxSum, node.val, node.val + l, \
                          node.val + r, node.val + l + r)
        return max(node.val, node.val + l, node.val + r)