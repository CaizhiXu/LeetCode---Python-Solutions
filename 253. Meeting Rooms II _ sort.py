## time - O(nlogn), space - O(n)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        timestamps = []
        res, curr = 0, 0

        for start, end in intervals:
            timestamps.append((start, 1))
            timestamps.append((end, -1))
        timestamps.sort()

        for t in timestamps:
            curr += t[1]
            res = max(res, curr)
        return res