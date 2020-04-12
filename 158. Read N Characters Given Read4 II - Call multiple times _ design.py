"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


## time - O(n), space - O(1)
class Solution:
    def __init__(self):
        self.tmp = [''] * 4
        self.idx = 0
        self.r = 0

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        idx = 0

        while n > 0:
            if self.idx == self.r:
                self.r = read4(self.tmp)
                self.idx = 0
                if not self.r:
                    return idx

            while self.idx < self.r and n > 0:
                buf[idx] = self.tmp[self.idx]
                idx += 1
                self.idx += 1
                n -= 1
        return idx   