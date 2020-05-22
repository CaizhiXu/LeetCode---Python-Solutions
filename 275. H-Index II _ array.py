## time - O(logn), space - O(1)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations or citations[-1] == 0:
            return 0
        if citations[0] >= len(citations):
            return len(citations)
        left, right = 1, len(citations)-1
        n = len(citations)
        while left < right:
            mid = left + (right-left)//2
            if citations[n-mid] >= mid and citations[n-mid-1] <= mid:
                return mid
            elif citations[n-mid] < mid:
                right = mid-1
            else:
                left = mid+1
        return right