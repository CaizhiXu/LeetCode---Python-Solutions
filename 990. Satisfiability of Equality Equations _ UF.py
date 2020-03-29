## time, space - O(N)
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX] < size[rootY]:
                    rootX, rootY = rootY, rootX
                parent[rootY] = rootX
                size[rootX] += size[rootY]

        parent, size = {}, {}
        notEquations = []
        for eq in equations:
            if eq[1:3] == '!=':
                notEquations.append([eq[0], eq[3]])
            else:
                if eq[0] not in parent:
                    parent[eq[0]] = eq[0]
                    size[eq[0]] = 1
                if eq[3] not in parent:
                    parent[eq[3]] = eq[3]
                    size[eq[3]] = 1
                union(eq[0], eq[3])

        for a, b in notEquations:
            if a == b:
                return False
            if a in parent and b in parent:
                if find(a) == find(b):
                    return False
        return True