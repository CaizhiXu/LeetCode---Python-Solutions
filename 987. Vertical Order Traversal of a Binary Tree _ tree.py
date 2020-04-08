# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time - O(nlogn), space - O(n)
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        vals = defaultdict(list)
        self.dfs(root, 0, 0, vals)

        results = []
        keys = sorted(vals.keys())
        for k in keys:
            vals[k].sort()
            tmp = [item[1] for item in vals[k]]
            results.append(tmp)
        return results

    def dfs(self, node, x, y, vals):
        if not node:
            return
        vals[x].append([y, node.val])
        self.dfs(node.left, x - 1, y + 1, vals)
        self.dfs(node.right, x + 1, y + 1, vals)