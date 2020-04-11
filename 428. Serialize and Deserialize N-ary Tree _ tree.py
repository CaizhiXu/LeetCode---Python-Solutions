"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
## time, space - O(n)
from collections import deque


class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if not root:
            return ''
        dq = deque([root])
        res = [root.val]
        res.append(None)
        while dq:
            node = dq.pop()
            for child in node.children:
                res.append(child.val)
                dq.appendleft(child)
            res.append(None)
        return " ".join(map(str, res))

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        data = data.split(' ')
        root = Node(int(data[0]), [])
        dq = deque([root])
        i = 2
        while dq and i < len(data):
            node = dq.pop()
            while data[i] != 'None':
                tmp = Node(int(data[i]), [])
                node.children.append(tmp)
                dq.appendleft(tmp)
                i += 1
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))