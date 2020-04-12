# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time, space - O(n)
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        if not root:
            return []
        curr, stack = root, []
        dq = deque()

        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                if len(dq) < k:
                    dq.append(node.val)
                else:
                    if abs(node.val - target) < abs(dq[0] - target):
                        dq.popleft()
                        dq.append(node.val)
                    else:
                        break
                curr = node.right
        return list(dq)