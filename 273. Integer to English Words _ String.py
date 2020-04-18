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


## time, space - O(n)
class Solution2:
    def numberToWords(self, num: int) -> str:
        numToStr1 = 'Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'
        numToStr2 = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'
        numToStr1 = numToStr1.split(' ')
        numToStr2 = numToStr2.split(' ')

        return self.helper(num, numToStr1, numToStr2)

    def helper(self, num, numToStr1, numToStr2):
        units = {10**3: "Thousand", 10**6: "Million", 10**9: "Billion"}
        if 0 <= num <= 19:
            return numToStr1[num]
        if num < 100:
            s = numToStr2[num // 10 - 2]
            if num % 10 != 0:
                s += ' ' + numToStr1[num % 10]
            return s
        if num < T:
            s = numToStr1[num // 100] + " Hundred"
            if num % 100 != 0:
                s += ' ' + self.helper(num % 100, numToStr1, numToStr2)
            return s

        for k in sorted(units.keys()):
            if num < k*1000:
                s = self.helper(num // k, numToStr1, numToStr2) + " " + units[k]
                if num % k != 0:
                    s += ' ' + self.helper(num % k, numToStr1, numToStr2)
                return s


### convert words to integers
class Convertion:
    def wordToInteger(self, words):
        ## converts words to integers and return them
        words = words.split(' ')
        multipliers = {'Thousand': 1000, 'Million': 1000000, 'Billion': 1000000000}

        pre = 0
        res = 0
        for i, w in enumerate(words):
            if w in multipliers:
                num = self.helper(words[pre:i])
                res += num * multipliers[w]
                pre = i + 1
        res += self.helper(words[pre:])
        return res

    def helper(self, words):
        if not words:
            return 0
        ## converts several words to a number
        strToNum = {'Zero':0, 'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, \
                    'Nine':9, 'Ten':10, 'Eleven':11, 'Twelve':12, 'Thirteen':13, 'Fourteen':14, 'Fifteen':15, \
                    'Sixteen':16, 'Seventeen':17, 'Eighteen':18, 'Nineteen':19, 'Twenty':20, 'Thirty':30, \
                    'Forty':40, 'Fifty':50, 'Sixty':60, 'Seventy':40, 'Eighty':80, 'Ninety':90}
        res = 0
        first = strToNum[words[0]]
        if len(words)>1 and words[1] == 'Hundred':
            res += first*100 + self.helper(words[2:])
        else:
            res += first + self.helper(words[1:])
        return res

sol = Convertion()
words = "One Billion One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
print(sol.wordToInteger(words))