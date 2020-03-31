# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## time - O(nlogn), space - O(logn)
class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(head2)
        return self.mergeSortList(l1, l2)

    def mergeSortList(self, h1, h2):
        dummy = ListNode(0)
        head = dummy
        while h1 and h2:
            if h1.val < h2.val:
                head.next = h1
                h1 = h1.next
            else:
                head.next = h2
                h2 = h2.next
            head = head.next
        head.next = h1 or h2
        return dummy.next



#time - O(nlogn), space - O(1)
class Solution(object):
    def sortList(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        step = 1
        length = 0
        while head:
            length += 1
            head = head.next

        while step < length:
            tail = dummy
            start = dummy.next
            while start:
                left_head = start
                right_head = self.moveByStep(left_head, step)
                start = self.moveByStep(right_head, step)

                while left_head and right_head:
                    if left_head.val < right_head.val:
                        tail.next = left_head
                        left_head = left_head.next
                    else:
                        tail.next = right_head
                        right_head = right_head.next
                    tail = tail.next
                tail.next = left_head or right_head
                while tail.next:
                    tail = tail.next
            step *= 2
        return dummy.next

    def moveByStep(self, node, step):
        while node and step > 1:
            node = node.next
            step -= 1
        if node:
            tmp, node.next = node.next, None
            return tmp
        else:
            return None