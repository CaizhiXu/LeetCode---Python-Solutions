# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        curr = [root]
        res = []
        while curr:
            curr_val = [node.val for node in curr]
            res.append(sum(curr_val)/len(curr_val))
            nxt_lvl, nxt_lvl_val = [], []
            for node in curr:
                if node.left:
                    nxt_lvl.append(node.left)
                    nxt_lvl_val.append(node.left.val)
                if node.right:
                    nxt_lvl.append(node.right)
                    nxt_lvl_val.append(node.right.val)
            curr = nxt_lvl
        return res