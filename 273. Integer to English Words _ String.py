## time, space - O(n)
class Solution:
    def numberToWords(self, num: int) -> str:
        s = str(num)
        n = len(s)
        res = []
        unit = {3: 'Thousand', 6: 'Million', 9: 'Billion'}

        k = n % 3
        while n > 0:
            if n % 3 != 0:
                first = self.helper(s[:k])
                n = n - k
            else:
                first = self.helper(s[k:k + 3])
                n = n - 3
                k += 3
            res.extend(first)
            if n != 0 and first:
                res.append(unit[n])
        return ' '.join(res)

    def helper(self, s):
        strToWord = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', \
                     '5': 'Five', '6': 'Six', '7': 'Seven', \
                     '8': 'Eight', '9': 'Nine', '10': 'Ten',
                     '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', \
                     '14': 'Fourteen', '15': 'Fifteen', '16': 'Sixteen', \
                     '17': 'Seventeen', '18': 'Eighteen', '19': 'Nineteen', \
                     '20': 'Twenty', '30': 'Thirty', '40': 'Forty', \
                     '50': 'Fifty', '60': 'Sixty', '70': 'Seventy', \
                     '80': 'Eighty', '90': 'Ninety'}

        if s == '0':
            return ['Zero']
        res = []
        n = len(s)

        while n > 0:
            if s[0] == '0':
                n -= 1
                s = s[1:]
                continue
            elif n == 3:
                res.append(strToWord[s[0]])
                res.append('Hundred')
                n -= 1
                s = s[1:]
            elif n == 2:
                if s in strToWord:
                    res.append(strToWord[s])
                    n -= 2
                else:
                    res.append(strToWord[s[0] + '0'])
                    n -= 1
                    s = s[1:]
            else:
                res.append(strToWord[s])
                n -= 1
        return res