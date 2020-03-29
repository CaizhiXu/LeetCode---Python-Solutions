## time, space - O(N)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nxt_dct = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                nxt_dct[stack[-1]] = num
                stack.pop()
            stack.append(num)

        res = []
        for num in nums1:
            if num in nxt_dct:
                res.append(nxt_dct[num])
            else:
                res.append(-1)
        return res