# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time, space  - O(n)
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        dep, node = self.depth(root)
        return node

    def depth(self, node):
        if not node:
            return 0, None
        ldep, lcan = self.depth(node.left)
        rdep, rcan = self.depth(node.right)
        if ldep == rdep:
            can = node
        elif ldep > rdep:
            can = lcan
        else:
            can = rcan
        return max(ldep, rdep) + 1, can