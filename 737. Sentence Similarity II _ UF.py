## time - O(len(pairs) + len(words1)), space - O(len(pairs))
class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if not words1 or not words2:
            return words1 == words2
        if len(words1) != len(words2):
            return False

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
        for a, b in pairs:
            if a not in parent:
                parent[a] = a
                size[a] = 1
            if b not in parent:
                parent[b] = b
                size[b] = 1
            union(a, b)

        for i in range(len(words1)):
            if words1[i] not in parent or words2[i] not in parent:
                if words1[i] != words2[i]:
                    return False
                else:
                    continue
            if find(words1[i]) != find(words2[i]):
                return False

        return True