# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## level-order representation
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        curr_lvl = [root]
        res = [root.val]
        while curr_lvl:
            nxt_lvl = []
            for node in curr_lvl:
                if node.left:
                    nxt_lvl.append(node.left)
                    res.append(node.left.val)
                else:
                    res.append(None)
                if node.right:
                    nxt_lvl.append(node.right)
                    res.append(node.right.val)
                else:
                    res.append(None)
            curr_lvl = nxt_lvl
        while res[-1] == None:
            res.pop()
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        root = TreeNode(data[0])
        n = len(data)
        curr_lvl = [root]
        s = 1
        while curr_lvl and s < n:
            nxt_lvl = []
            for node in curr_lvl:
                if data[s] != None:
                    node.left = TreeNode(data[s])
                    nxt_lvl.append(node.left)
                s += 1
                if s >= n:
                    break
                if data[s] != None:
                    node.right = TreeNode(data[s])
                    nxt_lvl.append(node.right)
                s += 1
                if s >= n:
                    break
            curr_lvl = nxt_lvl
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))