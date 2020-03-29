"""
Give a 2D matrix filled with "0" and "1", find out how many rectangles filled with "1"

"""


## dp, time - O(MN), space - O(m+n)
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        height, left, right = [0] * n, [0] * n, [n - 1] * n
        maxA = 0

        for i in range(m):
            curr_left, curr_right = 0, n - 1
            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] += 1
                    left[j] = max(left[j], curr_left)
                else:
                    height[j] = 0
                    left[j], curr_left = 0, j + 1
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], curr_right)
                else:
                    right[j], curr_right = n - 1, j - 1

            for j in range(n):
                maxA = max(maxA, (right[j] - left[j] + 1) * height[j])
        return maxA

    def numRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        height, left, right = [0] * n, [0] * n, [n - 1] * n
        res = set()
        rectangles = set()

        for i in range(m):
            curr_left, curr_right = 0, n - 1
            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] += 1
                    left[j] = max(left[j], curr_left)
                else:
                    height[j] = 0
                    left[j], curr_left = 0, j + 1
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], curr_right)
                else:
                    right[j], curr_right = n - 1, j - 1

            for j in range(n):
                if height[j] != 0:
                    rectangles.add((left[j], right[j], i, height[j]))

        for a, b, i, h in rectangles:
            for top in range(i-h+1, i+1):
                for l in range(a, b+1):
                    for r in range(l, b+1):
                        res.add((l, r, top, i))

        print(res)
        return len(res)

    """
    Given a 2D matrix filled with "0" and "1", find out how many rectangles filled with "1"

    """
## sol1, time - O(MNMN)
    def numRectangle_v1(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = 0

        for row in range(m):
            for col in range(n):
                col_limit = n
                for r in range(row, m):
                    if matrix[r][col] == "0":
                        break
                    for c in range(col, col_limit):
                        if matrix[r][c] == "0":
                            col_limit = c
                            break
                        res += 1
        return res

    """
    Given a 2D matrix filled with "0" and "1", find out how many rectangles filled with "1"

    """
    ## sol2, time - O(MMN)
    def numRectangle_v2(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        left = [[0]*n for i in range(m)]
        res = 0

        for i in range(m):
            curr_left = 0
            for j in range(n):
                if matrix[i][j] == "0":
                    left[i][j] = 0
                    curr_left = j + 1
                else:
                    left[i][j] = curr_left

                left_pos = left[i][j]
                for h in range(i, -1, -1):
                    if matrix[h][j] == '0':
                        break
                    left_pos = max(left_pos, left[h][j])
                    res += j - left_pos + 1
        return res

    ##
    def numRectangle_v2(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        left = [[0]*n for i in range(m)]
        res = 0

        for i in range(m):
            curr_left = 0
            for j in range(n):
                if matrix[i][j] == "0":
                    left[i][j] = 0
                    curr_left = j + 1
                else:
                    left[i][j] = curr_left

                left_pos = left[i][j]
                for h in range(i, -1, -1):
                    if matrix[h][j] == '0':
                        break
                    left_pos = max(left_pos, left[h][j])
                    res += j - left_pos + 1
        return res

sol = Solution()
grid = [["1","0","1","0","0"],["1","0","1","1","1"],["1","0","1","1","1"]]
print(sol.numRectangle_v1(grid))
print(sol.numRectangle_v2(grid))