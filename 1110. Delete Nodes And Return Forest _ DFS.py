# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_del = set(to_delete)

        def dfs(node):
            if node == None:
                return
            dfs(node.left)
            dfs(node.right)
            if node.val in to_del:
                if node.left and node.left.val not in to_del:
                    res.append(node.left)
                if node.right and node.right.val not in to_del:
                    res.append(node.right)
            if node.left and node.left.val in to_del:
                node.left = None
            if node.right and node.right.val in to_del:
                node.right = None

        dfs(root)
        if root.val not in to_del:
            res += [root]
        return res