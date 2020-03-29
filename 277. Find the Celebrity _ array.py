# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
## time - O(n), space - o(1)
class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(n):
            if knows(candidate, i):
                candidate = i
        for i in range(candidate):
            if knows(candidate, i):
                return -1
        for i in range(n):
            if not knows(i, candidate):
                return -1
        return candidate