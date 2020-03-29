## time, space - O(n), bucket sort
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        _min, _max = min(nums), max(nums)
        interval = (_max - _min) / (n - 1)
        if interval == 0:
            return 0

        maxInterval = [-float('inf')] * n
        minInterval = [float('inf')] * n
        for num in nums:
            idx = int((num - _min) / interval)
            maxInterval[idx] = max(maxInterval[idx], num)
            minInterval[idx] = min(minInterval[idx], num)

        gap = 0
        prev = _min
        for i in range(n):
            if minInterval[i] == float('inf'):
                continue
            gap = max(gap, minInterval[i] - prev)
            prev = maxInterval[i]
        return gap