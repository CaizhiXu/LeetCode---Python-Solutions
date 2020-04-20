## Type I
import random
class Solution:
    def findKthSmallest(self, nums, k):

        l, r = 0, len(nums)-1

        while True:
            pos = self.partition(nums, l, r)
            print(nums)
            if k > pos + 1:
                l = pos+1
            elif k < pos + 1:
                r = pos-1
            else:
                return nums[pos]

    # choose the right-most element as pivot
    def partition(self, nums, l, r):
        ran = random.randint(l,r)
        nums[ran], nums[r] = nums[r], nums[ran]
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low

nums = [3, 1, 1.5, 2.5, 3, 1, 2, 3, 5, 6, 4, 3, 3]
sol = Solution()
sol.findKthSmallest(nums, 5)


## Type II
from random import randint

class Solution2(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def partition(l, r):
            ri = randint(l, r)
            nums[r], nums[ri] = nums[ri], nums[r]
            for i, v in enumerate(nums[l: r + 1], l):
                if v >= nums[r]:
                    nums[l], nums[i] = nums[i], nums[l]
                    l += 1
            return l - 1

        l, r, k = 0, len(nums) - 1, k - 1
        while True:
            pos = partition(l, r)
            if pos < k:
                l = pos + 1
            elif pos > k:
                r = pos - 1
            else:
                return nums[pos]

