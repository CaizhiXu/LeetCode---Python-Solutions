class Heap:
    def __init__(self):
        pass

    def heapify(self, nums):
        if not nums:
            return
        n = len(nums)

        for i in range(n, -1, -1):
            self._heapify(nums, n, i)

    def _heapify(self, nums, n, i):  ## percolation downwards
        largest = i
        l = 2*i+1
        r = 2*i+2

        if l < n and nums[i] < nums[l]:
            largest = l
        if r < n and nums[i] < nums[r]:
            largest = r

        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self._heapify(nums, n, largest)

    def heapsort(self, nums):
        if not nums:
            return
        self.heapify(nums)

        n = len(nums)
        for i in range(n - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self._heapify(nums, i, 0)


nums = [3, 2, 5, 4, 8, 9, 1]
h = Heap()
h.heapsort(nums)
print(nums)