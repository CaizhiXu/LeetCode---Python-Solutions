from collections import Counter


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if not s:
            return ''
        ch_cnt = Counter(s)
        ch_freqRank = sorted(ch_cnt.items(), key=lambda x: x[1], reverse=True)

        maxCnt = ch_freqRank[0][1]
        if maxCnt == 1:
            return s
        res = [''] * maxCnt
        start = 0
        for ch, cnt in ch_freqRank:
            if cnt == maxCnt:
                for i in range(len(res)):
                    res[i] = res[i] + ch
            else:
                for j in range(start, start + cnt):
                    res[j % (maxCnt - 1)] += ch
                start += cnt
        if len(res[maxCnt - 2]) < k:
            return ''
        else:
            return ''.join(res)