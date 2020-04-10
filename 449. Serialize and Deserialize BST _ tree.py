# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:  # time, space - O(n)
        """Encodes a tree to a single string.
        """

        def postOrder(node):
            if not node:
                return []
            return postOrder(node.left) + postOrder(node.right) + [str(node.val)]

        res = postOrder(root)
        return ' '.join(res)

    def deserialize(self, data: str) -> TreeNode:  # time, space - O(n)
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        data = [int(s) for s in data.split(' ')]
        root = self.buildBSTTree(data, -float('inf'), float('inf'))
        return root

    def buildBSTTree(self, data, lower, upper):
        if not data or data[-1] < lower or data[-1] > upper:
            return None
        val = data.pop()
        root = TreeNode(val)

        root.right = self.buildBSTTree(data, val, upper)
        root.left = self.buildBSTTree(data, lower, val)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))