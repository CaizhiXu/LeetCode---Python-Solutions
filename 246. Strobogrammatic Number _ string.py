## time - O(n), space - O(1)
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        if not num:
            return True
        _map = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}

        n = len(num)
        for i in range((n + 1) // 2):
            if num[i] not in _map or num[n - 1 - i] not in _map:
                return False
            if num[i] != _map[num[n - 1 - i]]:
                return False
        return True