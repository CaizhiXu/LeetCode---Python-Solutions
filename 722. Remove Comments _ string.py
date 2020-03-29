## time, space - O(N)
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        buffer = ''
        block_comment_open = False
        res = []

        for line in source:
            i = 0
            while i < len(line):
                if not block_comment_open:
                    if line[i] == '/' and i + 1 < len(line) and line[i + 1] == '/':
                        i = len(line)
                    elif line[i] == '/' and i + 1 < len(line) and line[i + 1] == '*':
                        block_comment_open = True
                        i += 1
                    else:
                        buffer += line[i]
                else:
                    if line[i] == '*' and i + 1 < len(line) and line[i + 1] == '/':
                        block_comment_open = False
                        i += 1
                i += 1
            if buffer and not block_comment_open:
                res.append(buffer)
                buffer = ''
        return res