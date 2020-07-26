# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
## time - O(Nlogk), space - O(1)
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        step = 1
        while step < len(lists):
            for i in range(0, len(lists) - step, step * 2):
                lists[i] = self.mergeLists(lists[i], lists[i + step])
            step *= 2
        return lists[0]

    def mergeLists(self, l1, l2):
        dummy = ListNode(-1)
        head = dummy
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 or l2
        return dummy.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    def mergeKLists(self, lists):
        if not lists:
            return None
        n = len(lists)

        while n > 1:
            gap = (n + 1) // 2
            for i in range(n - gap):
                lists[i] = self.mergeLists(lists[i], lists[i + gap])
            n = gap
        return lists[0]

    def mergeLists(self, l1, l2):
        dummy = ListNode(-1)
        head = dummy
        while l1 or l2:
            n1 = l1.val if l1 else float('inf')
            n2 = l2.val if l2 else float('inf')
            if n1 <= n2:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        return dummy.next