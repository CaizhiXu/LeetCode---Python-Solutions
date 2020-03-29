# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        i = rand7()
        j = rand7()
        num = (i-1)*7 + j
        while num > 40:
            i = rand7()
            j = rand7()
            num = (i-1)*7 + j
        return (num-1)%10 + 1