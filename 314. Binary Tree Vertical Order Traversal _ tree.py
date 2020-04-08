# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time - O(nlogn), space - O(n)
from collections import deque, defaultdict


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        dq = deque()
        dq.append((0, root))
        xdct = defaultdict(list)

        while dq:
            x, node = dq.pop()
            xdct[x].append(node.val)
            if node.left:
                dq.appendleft((x - 1, node.left))
            if node.right:
                dq.appendleft((x + 1, node.right))

        keys = sorted(xdct.keys())
        res = [xdct[k] for k in keys]
        return res