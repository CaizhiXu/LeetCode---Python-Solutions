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