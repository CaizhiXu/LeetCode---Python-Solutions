## time - O(nlogn), space - O(nm)
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        vote_cnt = {}
        n = len(votes[0])
        for v in votes:
            for i, c in enumerate(v):
                if c not in vote_cnt:
                    vote_cnt[c] = [0]*n
                vote_cnt[c][i] += -1
        res = sorted(vote_cnt.keys(), key = lambda k:vote_cnt[k]+[k])
        return "".join(res)