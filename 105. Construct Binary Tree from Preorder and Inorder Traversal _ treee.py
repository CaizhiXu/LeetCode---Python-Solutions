# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time - O(n), space - O(n)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        idx_map = {inorder[i]: i for i in range(len(inorder))}
        return self.buildTreeHelper(preorder, 0, len(preorder) - 1, 0, idx_map)

    def buildTreeHelper(self, preorder, left, right, start, idx_map):
        if right < left:
            return None
        root = TreeNode(preorder[left])
        left_len = idx_map[root.val] - start
        root.left = self.buildTreeHelper(preorder, left + 1, \
                                         left + left_len, start, idx_map)
        root.right = self.buildTreeHelper(preorder, left + left_len + 1, \
                                          right, idx_map[root.val] + 1, idx_map)
        return root