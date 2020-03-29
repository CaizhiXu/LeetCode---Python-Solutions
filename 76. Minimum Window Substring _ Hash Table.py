class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = float('inf')
        minstr = ''
        sourcehash = [0] * 256
        targethash = [0] * 256
        self.init_target_hash(targethash, t)
        j = 0
        for i in range(len(s)):
            while not self.valid(sourcehash, targethash) and j < len(s):
                sourcehash[ord[j]] += 1
                j += 1
            if self.valid(sourcehash, targethash):
                if ans > j - i:
                    ans = j - i
                    minstr = s[i:j]
            sourcehash[ord[i]] -= 1
        return minstr

    def init_target_hash(self, targethash, t):
        for ch in t:
            targethash[ord[ch]] = targethash.get(ord[ch], 0) + 1

    def valid(self, sourcehash, targethash):  # to check whether it is includes in targethash
        for i in range(256):
            if targethash[i] > sourcehash[i]:
                return False
            return True


## time, space - O(N)
from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_cnts = Counter(t)
        s_cnts = defaultdict(int)
        start, end = 0, 0
        match = 0
        minstr = ''
        minLen = float('inf')

        while end < len(s):
            s_cnts[s[end]] += 1
            if s[end] in t_cnts and s_cnts[s[end]] == t_cnts[s[end]]:
                match += 1
            end += 1

            while match == len(t_cnts):
                if end - start < minLen:
                    minLen = end - start
                    minstr = s[start:end]
                s_cnts[s[start]] -= 1
                if s[start] in t_cnts and s_cnts[s[start]] < t_cnts[s[start]]:
                    match -= 1
                start += 1
        return minstr