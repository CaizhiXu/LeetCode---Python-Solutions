## time, space - O(MN)
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        res = set()
        morse_codes = [".-", "-...", "-.-.", "-..", ".", "..-.", \
                       "--.", "....", "..", ".---", "-.-", ".-..", \
                       "--", "-.", "---", ".--.", "--.-", ".-.", "...", \
                       "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        for w in words:
            temp = []
            for ch in w:
                temp.append(morse_codes[ord(ch) - ord('a')])
            res.add(''.join(temp))
        return len(res)
