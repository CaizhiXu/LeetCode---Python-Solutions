class Solution:
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':
        def backtrack(index, pre_op, curr_op, value, string):
            if index == len(num):
                if value == target and curr_op == 0:
                    res.append(''.join(string[1:]))
                return

            curr_op = curr_op * 10 + int(num[index])
            if curr_op > 0:
                backtrack(index + 1, pre_op, curr_op, value, string)

            string.append('+')
            string.append(str(curr_op))
            backtrack(index + 1, curr_op, 0, value + curr_op, string)
            string.pop()
            string.pop()

            if string:
                string.append('-')
                string.append(str(curr_op))
                backtrack(index + 1, -curr_op, 0, value - curr_op, string)
                string.pop()
                string.pop()

                string.append('*')
                string.append(str(curr_op))
                backtrack(index + 1, pre_op * curr_op, 0, value - pre_op + \
                          pre_op * curr_op, string)
                string.pop()
                string.pop()

        res = []
        backtrack(0, 0, 0, 0, [])
        return res


