# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
## time - O(n), space - O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        nodeA, nodeB = headA, headB
        while True:
            while nodeA and nodeB:
                if nodeA == nodeB:
                    return nodeA
                nodeA = nodeA.next
                nodeB = nodeB.next
            if nodeA == nodeB:
                return nodeA
            if not nodeA:
                nodeA = headB
            if not nodeB:
                nodeB = headA