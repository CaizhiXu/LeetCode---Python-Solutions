## time, space - O(nlogn), n = log(H-L)
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []

        for i in range(1, 9):
            num, d = 0, i
            while num <= high and d <= 9:
                num = 10 * num + d
                d += 1
                if low <= num <= high:
                    res.append(num)

        return sorted(res)