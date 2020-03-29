# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time, space - O(n)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node):
            if not node:
                return True, float("inf"), -float('inf')
            l_res = helper(node.left)
            r_res = helper(node.right)
            if not l_res[0] or not r_res[0]:
                return False, -1, -1
            if l_res[2] >= node.val or r_res[1] <= node.val:
                return False, -1, -1
            return True, min(node.val, l_res[1]), max(node.val, r_res[2])

        if not root:
            return True
        return helper(root)[0]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## time, space - O(N)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        lower = -float('inf')
        upper = float('inf')

        def helper(node, lower, upper):
            if not node:
                return True
            if not lower < node.val < upper:
                return False
            l_res = helper(node.left, lower, node.val)
            r_res = helper(node.right, node.val, upper)
            if not l_res or not r_res:
                return False
            return True

        return helper(root, lower, upper)