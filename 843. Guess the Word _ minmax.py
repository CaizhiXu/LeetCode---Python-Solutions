# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        idx = 0
        while idx < 10:
            n = len(wordlist)
            match = [[0] * n for i in range(n)]
            for i in range(n):
                for j in range(i, n):
                    match[i][j] = self.findmatch(wordlist[i], wordlist[j])
                    match[j][i] = match[i][j]
            min_cnt = n
            guess_idx = 0
            for i in range(n):
                cnt = 0
                for j in range(n):
                    if match[i][j] == 0:
                        cnt += 1
                if cnt < min_cnt:
                    min_cnt = cnt
                    guess_idx = i

            score = master.guess(wordlist[guess_idx])
            if score == 6:
                return wordlist[guess_idx]

            wordlist = [wordlist[j] for j in range(n) if match[guess_idx][j] == score]
            idx += 1

    def findmatch(self, word1, word2):
        cnt = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                cnt += 1
        return cnt