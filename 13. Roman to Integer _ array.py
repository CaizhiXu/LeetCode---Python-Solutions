class Solution:
    def romanToInt(self, s: str) -> int:
        val_dct = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, \
                   'D': 500, 'M': 1000}

        res = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and val_dct[s[i]] < val_dct[s[i + 1]]:
                res += -val_dct[s[i]] + val_dct[s[i + 1]]
                i += 2
            else:
                res += val_dct[s[i]]
                i += 1
        return res