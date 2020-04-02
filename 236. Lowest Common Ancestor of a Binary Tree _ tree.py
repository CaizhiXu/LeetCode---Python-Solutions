# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time - O(N), space - O(logn)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        self.res = None
        self.postOrder(root, p, q)
        return self.res

    def postOrder(self, node, p, q):
        if not node:
            return False
        left = self.postOrder(node.left, p, q)
        right = self.postOrder(node.right, p, q)
        if left or right:
            if left and right:
                self.res = node
            elif node == p or node == q:
                self.res = node
        return left or right or node == p or node == q