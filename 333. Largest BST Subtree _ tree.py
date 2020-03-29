# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time, space - O(N)
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.res = 1
        if not root:
            return 0
        self.postOrder(root)
        return self.res

    def postOrder(self, node):
        if not node:
            return True, float('inf'), -float('inf'), 0
        isBST_left, low_left, high_left, numNode_left = \
            self.postOrder(node.left)
        isBST_right, low_right, high_right, numNode_right = \
            self.postOrder(node.right)

        if not isBST_left or not isBST_right:
            return False, -1, -1, -1
        if node.val <= high_left or node.val >= low_right:
            return False, -1, -1, -1
        low = min(low_left, node.val)
        high = max(high_right, node.val)
        self.res = max(self.res, 1 + numNode_left + numNode_right)
        return True, low, high, 1 + numNode_left + numNode_right