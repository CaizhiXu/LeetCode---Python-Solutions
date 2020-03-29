class Solution:
    def removeStones(self, stones):
        X, Y = {}, {}
        parent = [i for i in range(len(stones))]

        def find(x):  ## searches for the root of node x
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        for i, pos in enumerate(stones):  ## union
            x, y = pos
            if x not in X:
                X[x] = i
            else:
                parent[i] = find(X[x])

            if y not in Y:
                Y[y] = i
            else:
                parent[find(i)] = find(Y[y])

        for i in range(len(parent)):  ## find
            find(i)
        print(parent)

        return len(stones) - len(set(parent))

stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
sol = Solution()
sol.removeStones(stones)
