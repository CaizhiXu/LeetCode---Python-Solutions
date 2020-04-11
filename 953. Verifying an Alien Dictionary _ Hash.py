## time - O(mn), space - O(1)
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dct = {order[i]: i for i in range(len(order))}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if not self.compare(w1, w2, order_dct):
                return False
        return True

    def compare(self, w1, w2, order_dct):
        for i in range(min(len(w1), len(w2))):
            if w1[i] == w2[i]:
                continue
            elif order_dct[w1[i]] > order_dct[w2[i]]:
                return False
            else:
                return True
        return i == len(w1) - 1