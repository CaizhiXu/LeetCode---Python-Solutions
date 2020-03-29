# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## time, space - O(MN)
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def traverse(Tnode):
            if not Tnode:
                return
            if Tnode.val == head.val:
                if dfs(Tnode, head):
                    return True
            if traverse(Tnode.left) or traverse(Tnode.right):
                return True
            return False

        def dfs(Tnode, Lnode):
            if not Lnode:
                return True
            if not Tnode:
                return False
            if Tnode.val != Lnode.val:
                return False
            if dfs(Tnode.left, Lnode.next) or dfs(Tnode.right, Lnode.next):
                return True
            else:
                return False

        return traverse(root)