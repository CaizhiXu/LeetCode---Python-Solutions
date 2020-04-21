## time, space - O(N)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, item in enumerate(intervals):
            if item[1] < newInterval[0]:
                res.append(item)
            elif item[0] > newInterval[1]:
                res.append(newInterval)
                res.append(item)
                return res + intervals[i + 1:]
            else:
                newInterval[0] = min(newInterval[0], item[0])
                newInterval[1] = max(newInterval[1], item[1])
        res.append(newInterval)

        return res