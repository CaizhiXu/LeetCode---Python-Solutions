## time - O(n), space - O(n)
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        preSum = [0]
        preSum_dct = {0:-1}
        maxLen = 0
        for i, num in enumerate(nums):
            currSum = preSum[-1]+num
            preSum.append(currSum)
            if currSum - k in preSum_dct:
                maxLen = max(maxLen, i-preSum_dct[currSum - k])
            if currSum not in preSum_dct:
                preSum_dct[currSum] = i
        return maxLen