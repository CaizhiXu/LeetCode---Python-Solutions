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







## Solution 2,
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        stack, curr = [], root
        res = []
        while stack or curr:
            if curr:
                res.append(str(curr.val))
                stack.append(curr)
                curr = curr.left
            else:
                res.append('None')
                curr = stack.pop()
                curr = curr.right
        print(res)
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(' ')
        root = TreeNode(int(data[0]))
        stack = [root]

        i, child = 1, 'left'
        curr = root
        while i < len(data):
            if data[i] != 'None':
                if child == 'left':
                    curr.left = TreeNode(int(data[i]))
                    stack.append(curr.left)
                    curr = curr.left
                else:
                    curr.right = TreeNode(int(data[i]))
                    stack.append(curr.right)
                    curr = curr.right
                    child = 'left'
            else:
                curr = stack.pop()
                child = 'right'
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec3:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def preOrder(node):
            if not node:
                return ['None']
            return [str(node.val)] + preOrder(node.left) + \
                   preOrder(node.right)

        return ' '.join(preOrder(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def preOrder(it):
            v = next(it)
            if v == 'None':
                return None
            node = TreeNode(int(v))
            node.left = preOrder(it)
            node.right = preOrder(it)
            return node

        data = data.split(' ')
        it = iter(data)
        return preOrder(it)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))