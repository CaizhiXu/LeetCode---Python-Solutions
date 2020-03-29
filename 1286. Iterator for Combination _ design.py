## time, space - O(1)
class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.generator = self.gen(characters, combinationLength)
        self.buffer = next(self.generator)

    def gen(self, string, length):
        if length == 0:
            yield ""
        elif len(string) == length:
            yield string
        else:
            for tail in self.gen(string[1:], length - 1):
                yield string[0] + tail
            for tail in self.gen(string[1:], length):
                yield tail

    def next(self) -> str:
        res = self.buffer
        try:
            self.buffer = next(self.generator)
        except:
            self.buffer = None
        return res

    def hasNext(self) -> bool:
        return self.buffer != None

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()