# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time, space - O(N)
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        curr_lvl = [root]
        while curr_lvl:
            nxt_lvl = []
            temp = []
            for node in curr_lvl:
                temp.append(node.val)
                if node.left:
                    nxt_lvl.append(node.left)
                if node.right:
                    nxt_lvl.append(node.right)
            curr_lvl = nxt_lvl
            res.append(temp)
        return res

