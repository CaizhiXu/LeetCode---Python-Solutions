## time - O(nlogn), space - O(1)
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort()
        cnt = 1
        boundary = points[0][1]
        for start, end in points[1:]:
            if start <= boundary:
                boundary = min(boundary, end)
                continue
            cnt += 1
            boundary = end
        return cnt