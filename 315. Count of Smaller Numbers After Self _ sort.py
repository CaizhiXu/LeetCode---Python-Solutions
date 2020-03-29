## time, space - O(nlogn)
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = list(enumerate(nums))
        res = [0] * len(nums)
        self.mergeSort(arr, res)
        return res

    def mergeSort(self, arr, res):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.mergeSort(arr[:mid], res)
        right = self.mergeSort(arr[mid:], res)

        i = len(arr) - 1
        while left and right:
            if left[-1][1] > right[-1][1]:
                res[left[-1][0]] += len(right)
                arr[i] = left.pop()
            else:
                arr[i] = right.pop()
            i -= 1
        while left:
            arr[i] = left.pop()
            i -= 1
        while right:
            arr[i] = right.pop()
            i -= 1
        return arr