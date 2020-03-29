## time, space - (2**n)
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []

        def helper(pos, curr, cnt):
            if pos == len(word):
                if cnt > 0:
                    res.append(curr + str(cnt))
                else:
                    res.append(curr)
                return
            helper(pos + 1, curr, cnt + 1)
            helper(pos + 1, curr + (str(cnt) if cnt > 0 else '') + word[pos], 0)

        helper(0, '', 0)
        return res