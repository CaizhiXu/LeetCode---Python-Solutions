# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
## time - O(n), space - O(n)
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        self.sum = 0
        self.inorder(root, L, R)
        return self.sum

    def inorder(self, node, L, R):
        if not node:
            return
        if L <= node.val <= R:
            self.sum += node.val
        if L < node.val:
            self.inorder(node.left, L, R)
        if R > node.val:
            self.inorder(node.right, L, R)