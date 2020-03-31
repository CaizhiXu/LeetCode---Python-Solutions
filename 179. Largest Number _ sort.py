## time - O(nlogn), space - O(logn)
import random
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return '0'
        self.quickSort(nums, 0, len(nums) - 1)
        return ''.join(map(str, nums))

    def quickSort(self, arr, left, right):
        if left >= right:
            return
        pos = self.partition(arr, left, right)
        self.quickSort(arr, left, pos - 1)
        self.quickSort(arr, pos + 1, right)

    def partition(self, arr, left, right):
        idx = random.randint(left, right)
        arr[right], arr[idx] = arr[idx], arr[right]
        low = left
        while left < right:
            if not self.compare(arr[left], arr[right]):
                arr[left], arr[low] = arr[low], arr[left]
                low += 1
            left += 1
        arr[low], arr[right] = arr[right], arr[low]
        return low

    def compare(self, num1, num2):
        if str(num1) + str(num2) < str(num2) + str(num1):
            return True
        else:
            return False