## time - O(N), space - O(1)
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        start, end = 0, 0
        currSum = 0
        minLen = float('inf')

        while end < len(nums):
            currSum += nums[end]
            while currSum >= s:
                minLen = min(minLen, end - start + 1)
                currSum -= nums[start]
                start += 1
            end += 1
        return minLen if minLen != float('inf') else 0


def find(self, x):
    if self.father[x] != x:
        self.father[x] = self.find(self.father[x])
    return self.father[x]