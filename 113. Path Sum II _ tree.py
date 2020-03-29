# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time, space - O(N)
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res, stack = [], []
        stack = [(root, root.val, [root.val])]
        while stack:
            curr, curr_sum, path = stack.pop()
            if curr.right:
                stack.append([curr.right, curr_sum + curr.right.val, \
                             path + [curr.right.val]])
            if curr.left:
                stack.append([curr.left, curr_sum + curr.left.val, \
                             path + [curr.left.val]])
            if not curr.left and not curr.right:
                if curr_sum == sum:
                    res.append(path)
        return res