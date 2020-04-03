# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time - O(N), space - O(N)
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        _, node = self.findNode(root)
        return node

    def findNode(self, node):
        if not node:
            return 0, None
        left_depth, left_can = self.findNode(node.left)
        right_depth, right_can = self.findNode(node.right)
        if left_depth == right_depth:
            return left_depth + 1, node
        elif left_depth > right_depth:
            return left_depth + 1, left_can
        else:
            return right_depth + 1, right_can