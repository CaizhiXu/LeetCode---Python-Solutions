## time - O(len(pairs)+len(words)), space - O(len(pairs))
from collections import defaultdict


class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if not words1 or not words2:
            return words1 == words2
        if len(words1) != len(words2):
            return False

        dct_pairs = defaultdict(list)
        for a, b in pairs:
            dct_pairs[a].append(b)
            dct_pairs[b].append(a)

        for i in range(len(words1)):
            if words1[i] == words2[i]:
                continue
            if words1[i] in dct_pairs:
                if words2[i] not in dct_pairs[words1[i]]:
                    return False
            else:
                return False
        return True