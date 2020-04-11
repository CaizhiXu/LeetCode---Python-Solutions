## time - O(n), space - O(1)
class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        maxIdx = 0
        numOn = 0
        cnt = 0
        for num in light:
            numOn += 1
            maxIdx = max(maxIdx, num)
            if maxIdx == numOn:
                cnt += 1
        return cnt