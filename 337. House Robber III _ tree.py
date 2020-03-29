# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time and space - O(N)
class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.maxSum(root))

    def maxSum(self, node):
        if not node:
            return [0, 0]  # withRoot, withoutRoot
        l = self.maxSum(node.left)
        r = self.maxSum(node.right)
        s1 = node.val + l[1] + r[1]
        s2 = max(l) + max(r)
        return [s1, s2]