## time - O(n**2), space - O(n)
class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        res = []
        self.helper(A, 0, len(A) - 1, res)
        return res

    def helper(self, arr, l, r, res):
        if l == r:
            return
        max_idx = l
        for i in range(l, r + 1):
            if arr[i] > arr[max_idx]:
                max_idx = i
        if max_idx != r:
            res.append(max_idx + 1)
            res.append(r + 1)
            self.flip(arr, l, max_idx)
            self.flip(arr, l, r)
        self.helper(arr, l, r - 1, res)

    def flip(self, arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1