class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations.sort(reverse = True)
        h_index = 0
        for i in range(len(citations)):
            if citations[i] >= i+1:
                continue
            else:
                return i
        return i+1