## time - O(nlogn), space - O(n), n is hard to obtain ...
class Solution:
    def expand(self, S: str) -> List[str]:
        res = []
        n = len(S)
        def helper(idx, curr):
            if idx == n:
                res.append(curr)
                return
            if S[idx] != '{':
                helper(idx+1, curr+S[idx])
            else:
                idx += 1
                tmp = []
                while S[idx] != '}':
                    if S[idx] != ',':
                        tmp.append(S[idx])
                    idx += 1
                for ch in tmp:
                    helper(idx+1, curr+ch)
        helper(0, '')
        return sorted(res)