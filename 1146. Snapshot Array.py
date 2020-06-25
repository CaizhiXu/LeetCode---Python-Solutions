## time - O(1) or O(nlogn), space - O(length * n), n is version number
class SnapshotArray:

    def __init__(self, length: int):
        self.array = [{0: 0} for _ in range(length)]
        self.snapid = 0

    def set(self, index: int, val: int) -> None:
        self.array[index][self.snapid] = val

    def snap(self) -> int:
        self.snapid += 1
        return self.snapid - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self.array[index]:
            return self.array[index][snap_id]
        ids = sorted(self.array[index].keys())
        key = self.binarySearch(ids, snap_id)
        return self.array[index][key]

    def binarySearch(self, nums, num):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= num < nums[mid + 1]:
                return nums[mid]
            elif num < nums[mid]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)