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


## time - O(N*4**N), space - O(N)
class Solution:
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':
        res = []
        self.target = target
        for i in range(1, len(num) + 1):
            if i == 1 or num[0] != '0':
                self.dfs(num[:i], num[i:], int(num[:i]), int(num[:i]), res)
        return res

    def dfs(self, path, arr, last, curr, res):
        if not arr:
            if curr == self.target:
                res.append(path)
            return
        for i in range(1, len(arr) + 1):
            if i == 1 or arr[0] != '0':
                tmp = arr[:i]
                self.dfs(path + '+' + tmp, arr[i:], int(tmp), curr + int(tmp), res)
                self.dfs(path + '-' + tmp, arr[i:], -int(tmp), curr - int(tmp), res)
                self.dfs(path + '*' + tmp, arr[i:], last * int(tmp), curr - last + last * int(tmp), res)
