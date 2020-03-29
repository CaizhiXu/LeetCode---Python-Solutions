# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time, space - O(N)
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        curr = root
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            if not stack:
                break
            node = stack.pop()
            res.append(node.val)
            curr = node.right
        return res