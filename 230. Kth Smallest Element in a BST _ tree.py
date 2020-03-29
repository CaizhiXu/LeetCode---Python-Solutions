# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time, space - O(n)
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        curr = root
        stack = []
        cnt = 0
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            if not stack:
                break
            node = stack.pop()
            curr = node.right
            cnt += 1
            if cnt == k:
                return node.val