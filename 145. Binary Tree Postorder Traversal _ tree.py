# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time, space - O(N)
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [root]
        while stack:
            curr = stack.pop()
            if curr:
                res.append(curr.val)
                stack.append(curr.left)
                stack.append(curr.right)
        res.reverse()
        return res