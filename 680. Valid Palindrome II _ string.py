## time - O(n), space - O(1)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                break
        if i == j:
            return True
        return self.isPalindrome(s[i + 1:j + 1]) or self.isPalindrome(s[i:j])

    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True


## time - O(n), space - O(1)
class Solution2:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True
        n = len(s)
        for i in range(n // 2):
            if s[i] == s[n - 1 - i]:
                continue
            else:
                return self.isPalindrome(s, i, n - 1 - i - 1) or \
                       self.isPalindrome(s, i + 1, n - 1 - i)
        return True

    def isPalindrome(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True