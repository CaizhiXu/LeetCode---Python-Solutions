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


class Solution(object):
    def sortList(self, head):
        dummy = ListNode(0)
        dummy.next = head
        step = 1
        length = 0
        while head:
            length += 1
            head = head.next

        while step < length:
            curr, tail = dummy.next, dummy
            while curr:
                left = curr
                for i in range(step - 1):
                    if not curr:
                        break
                    curr = curr.next
                if curr:
                    right, curr.next = curr.next, None
                    curr = right
                else:
                    right = None

                for i in range(step - 1):
                    if not curr:
                        break
                    curr = curr.next
                if curr:
                    temp, curr.next = curr.next, None
                    curr = temp

                while left and right:
                    if left.val < right.val:
                        tail.next, left = left, left.next
                    else:
                        tail.next, right = right, right.next
                    tail = tail.next
                tail.next = left or right
                while tail.next:
                    tail = tail.next

            step *= 2
        return dummy.next