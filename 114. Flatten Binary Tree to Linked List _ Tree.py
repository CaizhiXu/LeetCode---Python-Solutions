# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## in-order traversal
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node.left = None
            if stack:
                node.right = stack[-1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time - O(n), space - O(1)

class Solution2:
    def flatten(self, root: TreeNode) -> None:
        self.helper(root)

    def helper(self, node):
        if not node:
            return None
        if not node.left and not node.right:
            return node

        lefttail = self.helper(node.left)
        righttail = self.helper(node.right)
        if lefttail:
            lefttail.right = node.right
            node.right = node.left
            node.left = None
        return righttail if righttail else lefttail
