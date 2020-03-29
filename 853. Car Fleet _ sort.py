class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0
        cars = sorted(zip(position, speed))
        position, speed = zip(*cars)
        res = 1
        t = (target - position[-1]) / speed[-1]

        for i in range(len(position) - 2, -1, -1):
            if (target - position[i]) / speed[i] > t:
                res += 1
                t = (target - position[i]) / speed[i]
        return res