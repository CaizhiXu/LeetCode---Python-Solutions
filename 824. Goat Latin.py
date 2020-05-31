## time - O(n), space - O(n)
class Solution:
    def toGoatLatin(self, S: str) -> str:
        if not S:
            return ''

        vowels = set(['a', 'e', 'i', 'o', 'u'])
        words = S.split(' ')
        for i, w in enumerate(words):
            if w[0].lower() not in vowels:
                words[i] = w[1:] + w[0]
            words[i] = words[i] + 'ma' + 'a' * (i + 1)
        return ' '.join(words)